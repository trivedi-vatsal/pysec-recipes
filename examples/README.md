# Example Configuration Files

This directory contains example configuration files for different scenarios and customizations of the Python Security Audit workflow.

## Basic Configuration

### requirements.txt

A basic example requirements file to test the workflow:

```txt
requests==2.28.1
flask==2.2.2
click==8.1.3
jinja2==3.1.2
```

## Advanced Configurations

### 1. Multi-file Scanning

Scan multiple requirements files (development, production, testing):

```yaml
# In .github/workflows/security-audit.yml
- name: Scan all requirements files
  run: |
    for req_file in requirements*.txt; do
      if [ -f "$req_file" ]; then
        echo "Scanning $req_file..."
        pip-audit -r "$req_file" --format json --output "audit-outputs/audit-$req_file.json" || true
      fi
    done
```

### 2. Ignore Specific Vulnerabilities

Ignore known false positives or vulnerabilities you've assessed:

```yaml
- name: Run pip-audit with exclusions
  run: |
    pip-audit -r requirements.txt \
      --ignore-vuln CVE-2023-12345 \
      --ignore-vuln GHSA-xxxx-xxxx-xxxx \
      --format json --output audit-outputs/audit-results.json
```

### 3. Custom Schedule

Different scheduling options:

```yaml
# Daily scans
schedule:
  - cron: "0 2 * * *"  # 2 AM UTC daily

# Twice weekly
schedule:
  - cron: "0 8 * * 1,4"  # Monday and Thursday 8 AM UTC

# Monthly on first Monday
schedule:
  - cron: "0 8 1-7 * 1"  # First Monday of each month
```

### 4. Integration with Pre-commit

Add to `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/pypa/pip-audit
    rev: v2.6.1
    hooks:
      - id: pip-audit
        args: ['--desc', '--format=json']
```

### 5. Docker Integration

Add to your `Dockerfile`:

```dockerfile
# Security audit during build
RUN pip install pip-audit
RUN pip-audit -r requirements.txt --desc

# Or as a separate stage
FROM python:3.11 as security-check
COPY requirements.txt .
RUN pip install pip-audit
RUN pip-audit -r requirements.txt
```

### 6. CI/CD Integration

Fail the pipeline on vulnerabilities:

```yaml
- name: Fail on critical vulnerabilities
  if: env.AUDIT_STATUS == 'vulnerabilities_found'
  run: |
    echo "Critical security vulnerabilities found!"
    echo "Failing the build to prevent deployment."
    exit 1
```

### 7. Slack/Teams Notifications

Add notifications to your workflow:

```yaml
- name: Notify on Slack
  if: env.AUDIT_STATUS == 'vulnerabilities_found'
  uses: 8398a7/action-slack@v3
  with:
    status: failure
    fields: repo,message,commit,author,action,eventName,ref,workflow
    text: "🚨 Security vulnerabilities found in ${{ github.repository }}"
  env:
    SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK }}
```

### 8. Matrix Strategy

Test multiple Python versions:

```yaml
jobs:
  security-audit:
    strategy:
      matrix:
        python-version: ["3.9", "3.10", "3.11", "3.12"]
    
    steps:
      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python-version }}
```

### 9. Private Package Registries

Scan packages from private registries:

```yaml
- name: Configure private registry
  run: |
    pip config set global.extra-index-url https://your-private-registry.com/simple/
    pip config set global.trusted-host your-private-registry.com

- name: Run pip-audit with private packages
  run: |
    pip-audit -r requirements.txt --index-url https://your-private-registry.com/simple/
```

### 10. Advanced Issue Management

Custom issue handling:

```yaml
- name: Advanced issue management
  uses: actions/github-script@v7
  with:
    script: |
      // Custom logic for issue assignment
      const criticalVulns = process.env.CRITICAL_VULN_COUNT || 0;
      
      if (criticalVulns > 0) {
        // Auto-assign to security team
        await github.rest.issues.addAssignees({
          owner: context.repo.owner,
          repo: context.repo.repo,
          issue_number: issueNumber,
          assignees: ['security-team-lead']
        });
        
        // Add priority label
        await github.rest.issues.addLabels({
          owner: context.repo.owner,
          repo: context.repo.repo,
          issue_number: issueNumber,
          labels: ['priority:high', 'security:critical']
        });
      }
```

## Environment-Specific Configurations

### Development Environment

```yaml
# .github/workflows/dev-security-audit.yml
name: Development Security Audit
on:
  pull_request:
    paths: ['requirements-dev.txt']

jobs:
  dev-audit:
    # ... scan development dependencies
```

### Production Environment

```yaml
# More strict settings for production
- name: Production security audit
  run: |
    pip-audit -r requirements.txt \
      --vulnerability-service all \
      --format json \
      --output audit-results.json
    
    # Fail immediately on ANY vulnerability in production
    if [ "$(jq '[.dependencies[].vulns[]] | length' audit-results.json)" -gt 0 ]; then
      echo "Production deployment blocked due to security vulnerabilities"
      exit 1
    fi
```

## Custom Scripts

### Vulnerability Severity Filter

Create a script to filter by severity:

```python
#!/usr/bin/env python3
import json
import sys

def filter_by_severity(audit_file, min_severity="MODERATE"):
    severities = ["LOW", "MODERATE", "HIGH", "CRITICAL"]
    min_level = severities.index(min_severity)
    
    with open(audit_file) as f:
        data = json.load(f)
    
    critical_vulns = []
    for dep in data.get('dependencies', []):
        for vuln in dep.get('vulns', []):
            severity = vuln.get('severity', 'UNKNOWN')
            if severity in severities and severities.index(severity) >= min_level:
                critical_vulns.append(vuln)
    
    return critical_vulns

if __name__ == "__main__":
    critical = filter_by_severity("audit-results.json", "HIGH")
    if critical:
        print(f"Found {len(critical)} high/critical vulnerabilities")
        sys.exit(1)
    else:
        print("No high/critical vulnerabilities found")
```

### Auto-fix with Testing

```bash
#!/bin/bash
# auto-fix-with-test.sh

echo "Running security audit..."
pip-audit -r requirements.txt

echo "Attempting automatic fixes..."
pip-audit -r requirements.txt --fix --dry-run > proposed-fixes.txt

if [ -s proposed-fixes.txt ]; then
    echo "Proposed fixes:"
    cat proposed-fixes.txt
    
    # Apply fixes
    pip-audit -r requirements.txt --fix
    
    # Run tests
    if python -m pytest; then
        echo "✅ Fixes applied successfully, tests pass"
        pip freeze > requirements.txt
    else
        echo "❌ Tests failed after applying fixes"
        git checkout requirements.txt
        exit 1
    fi
else
    echo "No fixes available"
fi
```

## Repository Structure Examples

### Monorepo Structure

```
monorepo/
├── .github/workflows/security-audit.yml
├── service-a/
│   └── requirements.txt
├── service-b/
│   └── requirements.txt
└── shared/
    └── requirements.txt
```

Workflow for monorepo:

```yaml
- name: Scan all services
  run: |
    find . -name "requirements.txt" -exec pip-audit -r {} \;
```

### Multi-environment Structure

```
project/
├── requirements/
│   ├── base.txt
│   ├── development.txt
│   ├── production.txt
│   └── testing.txt
└── .github/workflows/
    ├── security-audit-prod.yml
    └── security-audit-dev.yml
```
