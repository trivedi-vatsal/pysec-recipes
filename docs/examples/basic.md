# Basic Recipe 🏠

The simplest way to add automated security auditing to your Python project. Perfect for getting started with zero configuration required.

!!! success "Perfect For"

    - **Simple Python projects** with a single `requirements.txt`
    - **Getting started** with security automation
    - **Single-environment** applications
    - **Straightforward dependency management**

## Project Structure

```bash title="Basic Project Structure"
my-python-project/
├── requirements.txt          # Your project dependencies
└── .github/
    └── workflows/
        └── security-audit.yml  # Security automation workflow
```

## Complete Workflow Configuration

???+ example "Complete security-audit.yml"

    This is the complete workflow file that provides automated security scanning for your basic Python project.

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
        branches: [main]
        paths:
          - "requirements.txt"
          - ".github/workflows/security-audit.yml"

    env:
      PYTHON_VERSION: "3.11"

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
            run: uv pip install --system pip-audit

          - name: Run pip-audit
            run: pip-audit -r requirements.txt --format json --output audit-results.json

          - name: Upload audit results
            uses: actions/upload-artifact@v4
            with:
              name: security-audit-results
              path: audit-results.json
    ```

## Quick Setup Instructions

Follow these simple steps to add security auditing to your project:

=== "One-Command Setup"

    !!! tip "Fastest Setup (Recommended)"

        Run this single command in your project root:

        ```bash title="One-command installation"
        curl -sSL https://raw.githubusercontent.com/trivedi-vatsal/pysec-recipes/main/setup.py | python3
        ```

        **What this does:**
        
        - ✅ Creates `.github/workflows/` directory
        - ✅ Downloads the complete workflow file
        - ✅ Sets up everything for automated security scanning

=== "Manual Setup"

    !!! example "Step-by-step manual installation"

        If you prefer to understand each step:

        1. **Create the workflow directory:**

            ```bash
            mkdir -p .github/workflows
            ```

        2. **Download the workflow file:**

            ```bash
            curl -o .github/workflows/security-audit.yml \
              https://raw.githubusercontent.com/trivedi-vatsal/pysec-recipes/main/.github/workflows/security-audit.yml
            ```

        3. **Ensure you have a requirements.txt file** in your project root

        4. **Commit and push** to trigger the workflow

## Verification Steps

After setup, verify everything is working:

!!! check "Test Your Setup"

    1. **Go to Actions tab** in your GitHub repository
    2. **Find the workflow** "Security Audit with pip-audit"  
    3. **Click "Run workflow"** → **"Run workflow"**
    4. **Watch the workflow run** - it should complete successfully

    **Expected Results:**
    - ✅ Workflow completes without errors
    - ✅ Artifacts uploaded (audit results)
    - ✅ Issues created if vulnerabilities found

## What Happens Next?

Once set up, your basic recipe will:

- **🔄 Run automatically** every Monday at 8 AM UTC
- **📱 Trigger on changes** to `requirements.txt`
- **🚨 Create GitHub issues** when vulnerabilities are found
- **📊 Upload detailed reports** as workflow artifacts
- **🔍 Scan all dependencies** for known security issues

## Ready for More?

Once you're comfortable with the basic recipe, consider upgrading:

- **[Django Recipe](django.md)** - For Django applications
- **[FastAPI Recipe](fastapi.md)** - For modern APIs  
- **[Enterprise Recipe](multi-environment.md)** - For multiple environments
- **[Monorepo Recipe](monorepo.md)** - For complex projects
