#!/usr/bin/env python3
"""
Python Security Audit Recipe Setup Script

This script helps you set up the Python Security Audit workflow in your repository.
It copies the necessary files and provides configuration options.

Usage:
    python setup.py [--branch BRANCH] [--python-version VERSION]
"""

import os
import sys
import argparse
import shutil
from pathlib import Path


def create_directory_structure(repo_root):
    """Create the necessary directory structure."""
    dirs = [".github/workflows", ".github/ISSUE_TEMPLATE"]

    for dir_path in dirs:
        full_path = repo_root / dir_path
        full_path.mkdir(parents=True, exist_ok=True)
        print(f"✅ Created directory: {dir_path}")


def copy_workflow_file(repo_root, branch="main", python_version="3.11"):
    """Copy and customize the workflow file."""
    workflow_content = f"""name: Security Audit with pip-audit

on:
  # Run weekly on Mondays at 8:00 AM UTC
  schedule:
    - cron: "0 8 * * 1"
  # Allow manual triggering
  workflow_dispatch:
  # Also run on pushes to main branch that change requirements.txt
  push:
    branches: [{branch}]
    paths:
      - "requirements.txt"
      - ".github/workflows/security-audit.yml"

env:
  PYTHON_VERSION: "{python_version}"

jobs:
  security-audit:
    name: Security Audit
    runs-on: ubuntu-latest
    permissions:
      contents: read
      issues: write
      security-events: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: ${{{{ env.PYTHON_VERSION }}}}

      - name: Install uv
        uses: astral-sh/setup-uv@v3

      - name: Install pip-audit with uv
        run: |
          uv pip install --system pip-audit

      - name: Run pip-audit (JSON output)
        id: audit-json
        run: |
          echo "Running pip-audit on requirements.txt..."

          # Create outputs directory
          mkdir -p audit-outputs

          # Run pip-audit with JSON output for processing
          pip-audit -r requirements.txt --format json --output audit-outputs/audit-results.json || echo "AUDIT_FAILED=true" >> $GITHUB_ENV

          # Also create human-readable formats
          pip-audit -r requirements.txt --format markdown --output audit-outputs/audit-results.md || true
          pip-audit -r requirements.txt --format columns --output audit-outputs/audit-results.txt || true

      - name: Process audit results
        id: process-results
        run: |
          # Check if audit results file exists
          if [ ! -f "audit-outputs/audit-results.json" ]; then
            echo "ERROR: Audit results file not found"
            echo "AUDIT_STATUS=error" >> $GITHUB_ENV
            exit 1
          fi

          # Parse JSON results
          VULN_COUNT=$(jq '[.dependencies[].vulns[]] | length' audit-outputs/audit-results.json)
          AFFECTED_PACKAGES=$(jq -r '.dependencies[] | select(.vulns | length > 0) | .name' audit-outputs/audit-results.json | wc -l)

          echo "VULN_COUNT=$VULN_COUNT" >> $GITHUB_ENV
          echo "AFFECTED_PACKAGES=$AFFECTED_PACKAGES" >> $GITHUB_ENV

          if [ "$VULN_COUNT" -eq 0 ]; then
            echo "AUDIT_STATUS=clean" >> $GITHUB_ENV
            echo "No vulnerabilities found!"
          else
            echo "AUDIT_STATUS=vulnerabilities_found" >> $GITHUB_ENV
            echo "Found $VULN_COUNT vulnerabilities in $AFFECTED_PACKAGES packages"
          fi

          # Create summary for issue body
          echo "## 🔍 Security Audit Summary" > audit-outputs/issue-body.md
          echo "" >> audit-outputs/issue-body.md
          echo "**Scan Date:** $(date -u +'%Y-%m-%d %H:%M:%S UTC')" >> audit-outputs/issue-body.md
          echo "**Repository:** ${{{{ github.repository }}}}" >> audit-outputs/issue-body.md
          echo "**Branch:** ${{{{ github.ref_name }}}}" >> audit-outputs/issue-body.md
          echo "**Commit:** ${{{{ github.sha }}}}" >> audit-outputs/issue-body.md
          echo "" >> audit-outputs/issue-body.md
          echo "**Vulnerabilities Found:** $VULN_COUNT" >> audit-outputs/issue-body.md
          echo "**Affected Packages:** $AFFECTED_PACKAGES" >> audit-outputs/issue-body.md
          echo "" >> audit-outputs/issue-body.md

          if [ "$VULN_COUNT" -gt 0 ]; then
            echo "## 🚨 Vulnerability Details" >> audit-outputs/issue-body.md
            echo "" >> audit-outputs/issue-body.md
            cat audit-outputs/audit-results.md >> audit-outputs/issue-body.md
            echo "" >> audit-outputs/issue-body.md
            echo "## 📋 Recommendations" >> audit-outputs/issue-body.md
            echo "" >> audit-outputs/issue-body.md
            echo "1. Review each vulnerability listed above" >> audit-outputs/issue-body.md
            echo "2. Update affected packages to the recommended fix versions" >> audit-outputs/issue-body.md
            echo "3. Test the application after updates" >> audit-outputs/issue-body.md
            echo "4. Consider using \\`pip-audit --fix\\` for automatic updates (with caution)" >> audit-outputs/issue-body.md
            echo "" >> audit-outputs/issue-body.md
            echo "## 🔧 Manual Fix Commands" >> audit-outputs/issue-body.md
            echo "" >> audit-outputs/issue-body.md
            echo "\\`\\`\\`bash" >> audit-outputs/issue-body.md
            echo "# Review the vulnerabilities" >> audit-outputs/issue-body.md
            echo "pip-audit -r requirements.txt" >> audit-outputs/issue-body.md
            echo "" >> audit-outputs/issue-body.md
            echo "# Attempt automatic fixes (use with caution)" >> audit-outputs/issue-body.md
            echo "pip-audit -r requirements.txt --fix" >> audit-outputs/issue-body.md
            echo "\\`\\`\\`" >> audit-outputs/issue-body.md
          else
            echo "✅ **No vulnerabilities detected in requirements.txt**" >> audit-outputs/issue-body.md
            echo "" >> audit-outputs/issue-body.md
            echo "All dependencies appear to be secure based on the current vulnerability databases." >> audit-outputs/issue-body.md
          fi

          echo "" >> audit-outputs/issue-body.md
          echo "---" >> audit-outputs/issue-body.md
          echo "*This issue was automatically generated by the Security Audit workflow.*" >> audit-outputs/issue-body.md
          echo "*Workflow run: [${{{{ github.run_id }}}}](${{{{ github.server_url }}}}/${{{{ github.repository }}}}/actions/runs/${{{{ github.run_id }}}})*" >> audit-outputs/issue-body.md

      - name: Upload audit artifacts
        uses: actions/upload-artifact@v4
        with:
          name: security-audit-results-${{{{ github.run_number }}}}
          path: audit-outputs/
          retention-days: 90

      - name: Create or update issue (vulnerabilities found)
        if: env.AUDIT_STATUS == 'vulnerabilities_found'
        uses: actions/github-script@v7
        with:
          github-token: ${{{{ secrets.GITHUB_TOKEN }}}}
          script: |
            const fs = require('fs');
            const path = require('path');

            // Read the issue body
            const issueBody = fs.readFileSync('audit-outputs/issue-body.md', 'utf8');

            // Check for existing open security audit issues
            const {{ data: issues }} = await github.rest.issues.listForRepo({{
              owner: context.repo.owner,
              repo: context.repo.repo,
              state: 'open',
              labels: 'security,pip-audit',
              per_page: 100
            }});

            const existingIssue = issues.find(issue =>
              issue.title.includes('Security Audit') &&
              issue.title.includes('vulnerabilities found')
            );

            const issueTitle = `🚨 Security Audit: ${{process.env.VULN_COUNT}} vulnerabilities found in dependencies`;

            if (existingIssue) {{
              // Update existing issue
              await github.rest.issues.update({{
                owner: context.repo.owner,
                repo: context.repo.repo,
                issue_number: existingIssue.number,
                title: issueTitle,
                body: issueBody,
                labels: ['security', 'pip-audit', 'vulnerability', 'dependencies']
              }});

              console.log(`Updated existing issue #${{existingIssue.number}}`);
            }} else {{
              // Create new issue
              const {{ data: newIssue }} = await github.rest.issues.create({{
                owner: context.repo.owner,
                repo: context.repo.repo,
                title: issueTitle,
                body: issueBody,
                labels: ['security', 'pip-audit', 'vulnerability', 'dependencies']
              }});

              console.log(`Created new issue #${{newIssue.number}}`);
            }}

      - name: Create clean audit issue (no vulnerabilities)
        if: env.AUDIT_STATUS == 'clean' && github.event_name == 'schedule'
        uses: actions/github-script@v7
        with:
          github-token: ${{{{ secrets.GITHUB_TOKEN }}}}
          script: |
            const fs = require('fs');

            // Read the issue body
            const issueBody = fs.readFileSync('audit-outputs/issue-body.md', 'utf8');

            // Close any existing vulnerability issues
            const {{ data: issues }} = await github.rest.issues.listForRepo({{
              owner: context.repo.owner,
              repo: context.repo.repo,
              state: 'open',
              labels: 'security,pip-audit',
              per_page: 100
            }});

            for (const issue of issues) {{
              if (issue.title.includes('vulnerabilities found')) {{
                await github.rest.issues.update({{
                  owner: context.repo.owner,
                  repo: context.repo.repo,
                  issue_number: issue.number,
                  state: 'closed',
                  state_reason: 'completed'
                }});

                await github.rest.issues.createComment({{
                  owner: context.repo.owner,
                  repo: context.repo.repo,
                  issue_number: issue.number,
                  body: '✅ Vulnerabilities have been resolved. This issue is now closed.'
                }});

                console.log(`Closed resolved issue #${{issue.number}}`);
              }}
            }}

            // Create a weekly clean report issue
            const {{ data: newIssue }} = await github.rest.issues.create({{
              owner: context.repo.owner,
              repo: context.repo.repo,
              title: `✅ Weekly Security Audit: No vulnerabilities found`,
              body: issueBody,
              labels: ['security', 'pip-audit', 'clean']
            }});

            // Auto-close the clean report issue after creation
            await github.rest.issues.update({{
              owner: context.repo.owner,
              repo: context.repo.repo,
              issue_number: newIssue.number,
              state: 'closed',
              state_reason: 'completed'
            }});

            console.log(`Created clean audit report issue #${{newIssue.number}} (auto-closed)`);

      - name: Comment on workflow status
        if: always()
        run: |
          echo "## 📊 Workflow Summary"
          echo "- **Status:** ${{{{ job.status }}}}"
          echo "- **Audit Status:** $AUDIT_STATUS"
          echo "- **Vulnerabilities Found:** ${{VULN_COUNT:-0}}"
          echo "- **Affected Packages:** ${{AFFECTED_PACKAGES:-0}}"
          echo "- **Trigger:** ${{{{ github.event_name }}}}"
          echo "- **Python Version:** ${{{{ env.PYTHON_VERSION }}}}"

      - name: Fail workflow if vulnerabilities found
        if: env.AUDIT_STATUS == 'vulnerabilities_found' && github.event_name != 'schedule'
        run: |
          echo "❌ Security vulnerabilities detected in dependencies!"
          echo "Check the created issue for details and remediation steps."
          exit 1
"""

    workflow_file = repo_root / ".github/workflows/security-audit.yml"
    with open(workflow_file, "w") as f:
        f.write(workflow_content)

    print(f"✅ Created workflow file: .github/workflows/security-audit.yml")
    print(f"   - Branch: {branch}")
    print(f"   - Python version: {python_version}")


def copy_issue_templates(repo_root):
    """Copy issue template files."""

    # Security vulnerability report template
    vuln_template = """---
name: Security Vulnerability Report
about: Automated security vulnerability report from pip-audit
title: "🚨 Security Audit: Vulnerabilities found in dependencies"
labels: ["security", "pip-audit", "vulnerability", "dependencies"]
assignees: []
---

## 🔍 Security Audit Summary

**Scan Date:** <!-- Date will be filled by workflow -->
**Repository:** <!-- Repository will be filled by workflow -->
**Branch:** <!-- Branch will be filled by workflow -->
**Commit:** <!-- Commit will be filled by workflow -->

**Vulnerabilities Found:** <!-- Count will be filled by workflow -->
**Affected Packages:** <!-- Count will be filled by workflow -->

## 🚨 Vulnerability Details

<!-- Vulnerability details will be filled by workflow -->

## 📋 Recommendations

1. Review each vulnerability listed above
2. Update affected packages to the recommended fix versions
3. Test the application after updates
4. Consider using `pip-audit --fix` for automatic updates (with caution)

## 🔧 Manual Fix Commands

```bash
# Review the vulnerabilities
pip-audit -r requirements.txt

# Attempt automatic fixes (use with caution)
pip-audit -r requirements.txt --fix
```

## ✅ Verification Steps

After applying fixes, verify the resolution by:

1. Running the security audit again:

   ```bash
   pip-audit -r requirements.txt
   ```

2. Running your test suite to ensure no breaking changes:

   ```bash
   # Add your test commands here
   python -m pytest
   ```

3. Testing key application functionality

## 📚 Additional Resources

- [pip-audit Documentation](https://github.com/pypa/pip-audit)
- [Python Security Advisories](https://github.com/pypa/advisory-database)
- [NIST National Vulnerability Database](https://nvd.nist.gov/)

---
*This issue was automatically generated by the Security Audit workflow.*
*Workflow run: View workflow details in Actions tab*
"""

    # Clean audit report template
    clean_template = """---
name: Clean Security Audit Report
about: Automated clean security report from pip-audit
title: "✅ Weekly Security Audit: No vulnerabilities found"
labels: ["security", "pip-audit", "clean"]
assignees: []
---

## 🔍 Security Audit Summary

**Scan Date:** <!-- Date will be filled by workflow -->
**Repository:** <!-- Repository will be filled by workflow -->
**Branch:** <!-- Branch will be filled by workflow -->
**Commit:** <!-- Commit will be filled by workflow -->

**Status:** ✅ **CLEAN** - No vulnerabilities detected

## 📊 Scan Results

All dependencies in `requirements.txt` have been scanned against the latest security vulnerability databases:

- **PyPI Advisory Database**
- **OSV (Open Source Vulnerabilities)**
- **Python Packaging Advisory Database**

No known security vulnerabilities were found in any of the project dependencies.

## 🛡️ Security Status

✅ All packages are up-to-date with security patches
✅ No known CVEs affecting current dependency versions
✅ Dependencies are from trusted sources

## 📈 Recommendations

Even though no vulnerabilities were found, consider these security best practices:

1. **Keep dependencies updated** - Regularly update to the latest stable versions
2. **Monitor security advisories** - Subscribe to security notifications for your dependencies
3. **Use dependency pinning** - Pin exact versions in production environments
4. **Regular audits** - This automated scan runs weekly to catch new vulnerabilities

## 🔄 Next Scan

The next automated security audit is scheduled for next Monday at 8:00 AM UTC.

---
*This clean audit report was automatically generated by the Security Audit workflow.*
*Workflow run: View workflow details in Actions tab*
"""

    # Write templates
    vuln_file = repo_root / ".github/ISSUE_TEMPLATE/security-vulnerability-report.md"
    with open(vuln_file, "w") as f:
        f.write(vuln_template)

    clean_file = repo_root / ".github/ISSUE_TEMPLATE/clean-security-audit-report.md"
    with open(clean_file, "w") as f:
        f.write(clean_template)

    print("✅ Created issue templates:")
    print("   - .github/ISSUE_TEMPLATE/security-vulnerability-report.md")
    print("   - .github/ISSUE_TEMPLATE/clean-security-audit-report.md")


def check_requirements_file(repo_root):
    """Check if requirements.txt exists."""
    req_file = repo_root / "requirements.txt"
    if req_file.exists():
        print("✅ Found requirements.txt file")
        return True
    else:
        print("⚠️  Warning: requirements.txt not found")
        print("   The workflow expects a requirements.txt file in the repository root")
        return False


def show_next_steps():
    """Show next steps to the user."""
    print("\n" + "=" * 60)
    print("🎉 Setup Complete!")
    print("=" * 60)
    print()
    print("Next steps:")
    print("1. Commit and push the new files to your repository")
    print("2. Ensure your repository has Issues enabled")
    print("3. Go to Actions tab and manually trigger the workflow to test")
    print("4. Check that the workflow has necessary permissions:")
    print("   - Settings → Actions → General → Workflow permissions")
    print("   - Should have 'Read and write permissions'")
    print()
    print("The workflow will:")
    print("• Run automatically every Monday at 8:00 AM UTC")
    print("• Run when requirements.txt changes")
    print("• Can be triggered manually from Actions tab")
    print()
    print("📚 For more details, see the README.md file")


def main():
    parser = argparse.ArgumentParser(
        description="Set up Python Security Audit workflow",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--branch", default="main", help="Default branch name (default: main)"
    )
    parser.add_argument(
        "--python-version", default="3.11", help="Python version to use (default: 3.11)"
    )

    args = parser.parse_args()

    # Get repository root
    repo_root = Path.cwd()

    print("🔧 Setting up Python Security Audit workflow...")
    print(f"📁 Repository: {repo_root}")
    print()

    # Create directory structure
    create_directory_structure(repo_root)

    # Copy workflow file
    copy_workflow_file(repo_root, args.branch, args.python_version)

    # Copy issue templates
    copy_issue_templates(repo_root)

    # Check for requirements.txt
    check_requirements_file(repo_root)

    # Show next steps
    show_next_steps()


if __name__ == "__main__":
    main()
