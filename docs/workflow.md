# Complete Workflow Code

!!! abstract "Complete Security Audit Workflow"

    This is the complete `security-audit.yml` workflow file that provides automated security scanning,
    intelligent issue management, and comprehensive reporting for your Python project.
 
    ??? info ".github/workflows/security-audit.yml"

        ```yaml title=".github/workflows/security-audit.yml" linenums="1"
        name: Security Audit with pip-audit

        on:
          # Run weekly on Mondays at 8:00 AM UTC
          schedule:
            - cron: "0 8 * * 1"
          # Allow manual triggering
          workflow_dispatch:
          # Also run on pushes to main branch that change requirements.txt
          push:
            branches: [main] # Update this to your default branch
            paths:
              - "requirements.txt"
              - ".github/workflows/security-audit.yml"

        env:
          PYTHON_VERSION: "3.11" # Update this to your preferred Python version

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
                  python-version: ${{ env.PYTHON_VERSION }}

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
                  pip-audit -r requirements.txt --format json --output audit-outputs/ audit-results.json || echo "AUDIT_FAILED=true" >> $GITHUB_ENV

                  # Also create human-readable formats
                  pip-audit -r requirements.txt --format markdown --output audit-outputs/ audit-results.md || true
                  pip-audit -r requirements.txt --format columns --output audit-outputs/  audit-results.txt || true

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
                  VULN_COUNT=$(jq '[.dependencies[].vulns[]] | length' audit-outputs/ audit-results.json)
                  AFFECTED_PACKAGES=$(jq -r '.dependencies[] | select(.vulns | length > 0) | .  name' audit-outputs/audit-results.json | wc -l)

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
                  echo "**Scan Date:** $(date -u +'%Y-%m-%d %H:%M:%S UTC')" >> audit-outputs/ issue-body.md
                  echo "**Repository:** ${{ github.repository }}" >> audit-outputs/issue-body.md
                  echo "**Branch:** ${{ github.ref_name }}" >> audit-outputs/issue-body.md
                  echo "**Commit:** ${{ github.sha }}" >> audit-outputs/issue-body.md
                  echo "" >> audit-outputs/issue-body.md
                  echo "**Vulnerabilities Found:** $VULN_COUNT" >> audit-outputs/issue-body.md
                  echo "**Affected Packages:** $AFFECTED_PACKAGES" >> audit-outputs/issue-body. md
                  echo "" >> audit-outputs/issue-body.md

                  if [ "$VULN_COUNT" -gt 0 ]; then
                    echo "## 🚨 Vulnerability Details" >> audit-outputs/issue-body.md
                    echo "" >> audit-outputs/issue-body.md
                    cat audit-outputs/audit-results.md >> audit-outputs/issue-body.md
                    echo "" >> audit-outputs/issue-body.md
                    echo "## 📋 Recommendations" >> audit-outputs/issue-body.md
                    echo "" >> audit-outputs/issue-body.md
                    echo "1. Review each vulnerability listed above" >> audit-outputs/  issue-body.md
                    echo "2. Update affected packages to the recommended fix versions" >>   audit-outputs/issue-body.md
                    echo "3. Test the application after updates" >> audit-outputs/issue-body.md
                    echo "4. Consider using \`pip-audit --fix\` for automatic updates (with   caution)" >> audit-outputs/issue-body.md
                    echo "" >> audit-outputs/issue-body.md
                    echo "## 🔧 Manual Fix Commands" >> audit-outputs/issue-body.md
                    echo "" >> audit-outputs/issue-body.md
                    echo "\`\`\`bash" >> audit-outputs/issue-body.md
                    echo "# Review the vulnerabilities" >> audit-outputs/issue-body.md
                    echo "pip-audit -r requirements.txt" >> audit-outputs/issue-body.md
                    echo "" >> audit-outputs/issue-body.md
                    echo "# Attempt automatic fixes (use with caution)" >> audit-outputs/ issue-body.md
                    echo "pip-audit -r requirements.txt --fix" >> audit-outputs/issue-body.md
                    echo "\`\`\`" >> audit-outputs/issue-body.md
                  else
                    echo "✅ **No vulnerabilities detected in requirements.txt**" >>  audit-outputs/issue-body.md
                    echo "" >> audit-outputs/issue-body.md
                    echo "All dependencies appear to be secure based on the current   vulnerability databases." >> audit-outputs/issue-body.md
                  fi

                  echo "" >> audit-outputs/issue-body.md
                  echo "---" >> audit-outputs/issue-body.md
                  echo "*This issue was automatically generated by the Security Audit workflow. *" >> audit-outputs/issue-body.md
                  echo "*Workflow run: [${{ github.run_id }}](${{ github.server_url }}/${{  github.repository }}/actions/runs/${{ github.run_id }})*" >> audit-outputs/  issue-body.md

              - name: Upload audit artifacts
                uses: actions/upload-artifact@v4
                with:
                  name: security-audit-results-${{ github.run_number }}
                  path: audit-outputs/
                  retention-days: 90

              - name: Create or update issue (vulnerabilities found)
                if: env.AUDIT_STATUS == 'vulnerabilities_found'
                uses: actions/github-script@v7
                with:
                  github-token: ${{ secrets.GITHUB_TOKEN }}
                  script: |
                    const fs = require('fs');
                    const path = require('path');

                    // Read the issue body
                    const issueBody = fs.readFileSync('audit-outputs/issue-body.md', 'utf8');

                    // Check for existing open security audit issues
                    const { data: issues } = await github.rest.issues.listForRepo({
                      owner: context.repo.owner,
                      repo: context.repo.repo,
                      state: 'open',
                      labels: 'security,pip-audit',
                      per_page: 100
                    });

                    const existingIssue = issues.find(issue =>
                      issue.title.includes('Security Audit') &&
                      issue.title.includes('vulnerabilities found')
                    );

                    const issueTitle = `🚨 Security Audit: ${process.env.VULN_COUNT}  vulnerabilities found in dependencies`;

                    if (existingIssue) {
                      // Update existing issue
                      await github.rest.issues.update({
                        owner: context.repo.owner,
                        repo: context.repo.repo,
                        issue_number: existingIssue.number,
                        title: issueTitle,
                        body: issueBody,
                        labels: ['security', 'pip-audit', 'vulnerability', 'dependencies']
                      });

                      console.log(`Updated existing issue #${existingIssue.number}`);
                    } else {
                      // Create new issue
                      const { data: newIssue } = await github.rest.issues.create({
                        owner: context.repo.owner,
                        repo: context.repo.repo,
                        title: issueTitle,
                        body: issueBody,
                        labels: ['security', 'pip-audit', 'vulnerability', 'dependencies']
                      });

                      console.log(`Created new issue #${newIssue.number}`);
                    }

              - name: Create clean audit issue (no vulnerabilities)
                if: env.AUDIT_STATUS == 'clean' && github.event_name == 'schedule'
                uses: actions/github-script@v7
                with:
                  github-token: ${{ secrets.GITHUB_TOKEN }}
                  script: |
                    const fs = require('fs');

                    // Read the issue body
                    const issueBody = fs.readFileSync('audit-outputs/issue-body.md', 'utf8');

                    // Close any existing vulnerability issues
                    const { data: issues } = await github.rest.issues.listForRepo({
                      owner: context.repo.owner,
                      repo: context.repo.repo,
                      state: 'open',
                      labels: 'security,pip-audit',
                      per_page: 100
                    });

                    for (const issue of issues) {
                      if (issue.title.includes('vulnerabilities found')) {
                        await github.rest.issues.update({
                          owner: context.repo.owner,
                          repo: context.repo.repo,
                          issue_number: issue.number,
                          state: 'closed',
                          state_reason: 'completed'
                        });

                        await github.rest.issues.createComment({
                          owner: context.repo.owner,
                          repo: context.repo.repo,
                          issue_number: issue.number,
                          body: '✅ Vulnerabilities have been resolved. This issue is now closed. '
                        });

                        console.log(`Closed resolved issue #${issue.number}`);
                      }
                    }

                    // Create a weekly clean report issue
                    const { data: newIssue } = await github.rest.issues.create({
                      owner: context.repo.owner,
                      repo: context.repo.repo,
                      title: `✅ Weekly Security Audit: No vulnerabilities found`,
                      body: issueBody,
                      labels: ['security', 'pip-audit', 'clean']
                    });

                    // Auto-close the clean report issue after creation
                    await github.rest.issues.update({
                      owner: context.repo.owner,
                      repo: context.repo.repo,
                      issue_number: newIssue.number,
                      state: 'closed',
                      state_reason: 'completed'
                    });

                    console.log(`Created clean audit report issue #${newIssue.number}   (auto-closed)`);

              - name: Comment on workflow status
                if: always()
                run: |
                  echo "## 📊 Workflow Summary"
                  echo "- **Status:** ${{ job.status }}"
                  echo "- **Audit Status:** $AUDIT_STATUS"
                  echo "- **Vulnerabilities Found:** ${VULN_COUNT:-0}"
                  echo "- **Affected Packages:** ${AFFECTED_PACKAGES:-0}"
                  echo "- **Trigger:** ${{ github.event_name }}"
                  echo "- **Python Version:** ${{ env.PYTHON_VERSION }}"

              - name: Fail workflow if vulnerabilities found
                if: env.AUDIT_STATUS == 'vulnerabilities_found' && github.event_name !=   'schedule'
                run: |
                  echo "❌ Security vulnerabilities detected in dependencies!"
                  echo "Check the created issue for details and remediation steps."
                  exit 1
        ```

## Key Steps Explained

### 1. Triggers

- **Weekly**: Runs every Monday at 8 AM UTC
- **Manual**: Can be triggered from GitHub Actions tab
- **Push**: Runs when `requirements.txt` changes

### 2. Audit Execution

```bash title="pip-audit execution with multiple formats"
# Creates JSON, Markdown, and text outputs
pip-audit -r requirements.txt --format json --output audit-results.json
pip-audit -r requirements.txt --format markdown --output audit-results.md
pip-audit -r requirements.txt --format columns --output audit-results.txt
```

### 3. Result Processing

Uses `jq` to parse JSON results and extract vulnerability counts:

```bash title="JSON parsing with jq"
VULN_COUNT=$(jq '[.dependencies[].vulns[]] | length' audit-results.json)
AFFECTED_PACKAGES=$(jq -r '.dependencies[] | select(.vulns | length > 0) | .name' audit-results.json | wc -l)
```

### 4. Issue Management

- Creates GitHub issues for vulnerabilities
- Updates existing issues with new scan results
- Auto-closes issues when vulnerabilities are resolved
- Creates weekly clean reports

---

???+ note "📚 Documentation Progress Checklist"

    Track your progress through the Python Security Audit Recipe documentation:

    - [x] **🏠 Home** - Understanding the security challenge
    - [x] **📖 Getting Started** - Quick overview and concepts  
    - [x] **⚙️ Installation** - Set up your environment
    - [x] **🔄 Workflow Details** - Understand GitHub Actions mechanics
    - [ ] **📋 Issue Templates** - Master security notification management
    - [ ] **🔧 Configuration** - Customize for your project needs
    - [ ] **📚 Examples** - Real-world implementations

### **Next Up:** [Issue Templates](issue-templates.md)

**Ready to master GitHub issue management?** Continue to **[Issue Templates](issue-templates.md)** to learn how security notifications are structured and customized!
