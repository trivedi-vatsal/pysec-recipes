# Installation

Install and set up the Python Security Audit Recipe in your GitHub repository with these simple steps.

## Prerequisites

Before installing, ensure you have:

- ✅ **GitHub repository** with a Python project
- ✅ **`requirements.txt` file** in your repository root  
- ✅ **GitHub Actions enabled** in your repository
- ✅ **Repository write access** to create workflows and issues

## Installation Options

???+ tip "Recommended: One-Command Setup"

    The fastest way to get started with automated security auditing for your Python project.

    === "One-Command Setup"

        Run this single command in your project root:

        ```bash
        curl -sSL https://raw.githubusercontent.com/trivedi-vatsal/pysec-recipes/main/setup.py | python3
        ```

        **What this does:**
        
        - ✅ Creates `.github/workflows/` and `.github/ISSUE_TEMPLATE/` directories
        - ✅ Downloads the complete workflow file (`security-audit.yml`)
        - ✅ Downloads vulnerability and clean audit issue templates
        - ✅ Sets up everything for automated security scanning

        **That's it!** Your repository now has automated security auditing.

    === "Manual Installation"

        If you prefer to understand each step or need custom setup:

        1. **Create directory structure:**

            ```bash
            mkdir -p .github/workflows .github/ISSUE_TEMPLATE
            ```

        2. **Download the workflow file:**

            ```bash
            curl -o .github/workflows/security-audit.yml \
              https://raw.githubusercontent.com/trivedi-vatsal/pysec-recipes/main/.github/workflows/security-audit.yml
            ```

        3. **Download issue templates:**

            ```bash
            # Vulnerability report template
            curl -o .github/ISSUE_TEMPLATE/security-vulnerability-report.md \
              https://raw.githubusercontent.com/trivedi-vatsal/pysec-recipes/main/.github/ISSUE_TEMPLATE/security-vulnerability-report.md

            # Clean audit report template  
            curl -o .github/ISSUE_TEMPLATE/clean-security-audit-report.md \
              https://raw.githubusercontent.com/trivedi-vatsal/pysec-recipes/main/.github/ISSUE_TEMPLATE/clean-security-audit-report.md
            ```

## Required Permissions Setup

!!! warning "Important: Repository Permissions"

    The workflow needs specific permissions to create and manage GitHub issues automatically.

**Setup Steps:**

1. Go to your repository **Settings** → **Actions** → **General**
2. Scroll down to **Workflow permissions**
3. Select **"Read and write permissions"**  
4. Check **"Allow GitHub Actions to create and approve pull requests"**

Without these permissions, the workflow can scan for vulnerabilities but cannot create or update issues.

## Verify Installation

After installation, test that everything works:

1. **Go to Actions tab** in your GitHub repository
2. **Find the workflow** "Security Audit with pip-audit"
3. **Click "Run workflow"** → **"Run workflow"**
4. **Watch the workflow run** - it should complete successfully

### Expected Results

- ✅ **Workflow completes** without errors
- ✅ **Artifacts uploaded** (audit results)  
- ✅ **Issue created** (if vulnerabilities found) or clean report
- ✅ **No permission errors** in the workflow logs

## What Gets Installed

After installation, your repository will have:

```
your-repo/
├── .github/
│   ├── workflows/
│   │   └── security-audit.yml          # Main workflow file
│   └── ISSUE_TEMPLATE/
│       ├── security-vulnerability-report.md    # Vulnerability issue template
│       └── clean-security-audit-report.md      # Clean audit issue template
└── requirements.txt                     # Your existing dependencies
```

## Automatic Schedule

The workflow is configured to run:

- **📅 Weekly** - Every Monday at 8:00 AM UTC
- **🔄 On changes** - When `requirements.txt` is updated  
- **🎛️ Manual** - Anytime via "Run workflow" button

## ⚠️ Troubleshooting

### Common Issues

!!! bug "Permission Denied Errors"

    **Problem:** Workflow fails with permission errors  
    **Solution:** Follow the [Repository Permissions Setup](#required-permissions-setup) above

!!! bug "Workflow Not Found"

    **Problem:** Can't find "Security Audit with pip-audit" in Actions tab  
    **Solution:** Check that `security-audit.yml` is in `.github/workflows/` directory

!!! bug "No Issues Created"

    **Problem:** Workflow runs but no issues appear  
    **Solution:** Verify repository permissions and check if vulnerabilities were actually found

---

???+ note "Documentation Progress Checklist"

    Track your progress through the Python Security Audit Recipe documentation:

    - [x] **Home** - Understanding the security challenge
    - [x] **Getting Started** - Quick overview and concepts  
    - [x] **Installation** - Set up your environment
    - [ ] **Workflow Details** - Understand GitHub Actions mechanics
    - [ ] **Issue Templates** - Master security notification management
    - [ ] **Configuration** - Customize for your project needs
    - [ ] **Examples** - Real-world implementations

### Next Up: [Workflow Details](workflow.md)

**Ready to understand how the automation works?** Continue to **[Workflow Details](workflow.md)** to learn the mechanics behind automated security scanning!
