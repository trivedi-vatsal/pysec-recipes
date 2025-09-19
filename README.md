# Python Security Audit Recipe 🔐

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-enabled-blue.svg)](https://github.com/features/actions)
[![pip-audit](https://img.shields.io/badge/security-pip--audit-red.svg)](https://github.com/pypa/pip-audit)

A ready-to-use GitHub Actions workflow recipe for automated Python dependency security auditing using `pip-audit`. This recipe provides comprehensive vulnerability scanning, intelligent issue management, and detailed reporting for Python projects.

## 🎯 Features

- **🔄 Automated Scanning**: Weekly scheduled scans + manual triggers
- **📊 Multiple Report Formats**: JSON, Markdown, and text outputs
- **🎫 Smart Issue Management**: Creates, updates, and closes security issues automatically
- **📁 Artifact Storage**: 90-day retention of detailed audit results
- **🛡️ Comprehensive Coverage**: Scans `requirements.txt` and dependency trees
- **⚡ Zero Configuration**: Works out-of-the-box with sensible defaults
- **🔧 Highly Customizable**: Easy to adapt for different project needs

## 🚀 Quick Start

### 1. Copy Files to Your Repository

```bash
# Create the directory structure
mkdir -p .github/workflows .github/ISSUE_TEMPLATE

# Copy the workflow file
curl -O https://raw.githubusercontent.com/trivedi-vatsal/python-security-audit-recipe/main/.github/workflows/security-audit.yml
mv security-audit.yml .github/workflows/

# Copy issue templates
curl -O https://raw.githubusercontent.com/trivedi-vatsal/python-security-audit-recipe/main/.github/ISSUE_TEMPLATE/security-vulnerability-report.md
curl -O https://raw.githubusercontent.com/trivedi-vatsal/python-security-audit-recipe/main/.github/ISSUE_TEMPLATE/clean-security-audit-report.md
mv *.md .github/ISSUE_TEMPLATE/
```

### 2. Customize for Your Project

Edit `.github/workflows/security-audit.yml` and update:

```yaml
# Change the default branch name if needed
branches: [main]  # or [master, develop, etc.]

# Adjust Python version
env:
  PYTHON_VERSION: "3.11"  # or your preferred version
```

### 3. Ensure Required Permissions

The workflow needs these repository permissions:

- ✅ **Issues**: Write access to create/update security issues
- ✅ **Actions**: Enabled to run the workflow
- ✅ **Contents**: Read access to scan your repository

### 4. Test the Setup

1. Go to **Actions** tab in your GitHub repository
2. Select **Security Audit with pip-audit**
3. Click **Run workflow** → **Run workflow**
4. Watch the workflow complete and check for any issues created

## 📋 What Gets Created

### Repository Structure

```markdown
your-repo/
├── .github/
│   ├── workflows/
│   │   └── security-audit.yml           # Main workflow
│   └── ISSUE_TEMPLATE/
│       ├── security-vulnerability-report.md
│       └── clean-security-audit-report.md
├── requirements.txt                     # Your dependencies (required)
└── [your project files]
```

### Generated Artifacts

- **Security Issues**: Detailed vulnerability reports with fix instructions
- **Audit Reports**: JSON, Markdown, and text format results
- **Workflow Artifacts**: Downloadable reports stored for 90 days

## 🔧 How It Works

### Workflow Triggers

1. **📅 Weekly Schedule**: Every Monday at 8:00 AM UTC
2. **🔄 Manual Trigger**: Via GitHub Actions interface
3. **📝 File Changes**: When `requirements.txt` or workflow file changes

### Security Scanning Process

1. **Environment Setup**: Python 3.11, latest `pip-audit`
2. **Dependency Scan**: Analyzes `requirements.txt` for vulnerabilities
3. **Report Generation**: Creates JSON, Markdown, and text reports
4. **Issue Management**: Creates/updates GitHub issues with findings
5. **Artifact Upload**: Stores detailed results for team review

### Issue Management Logic

**When Vulnerabilities Found** 🚨:

- Creates new security issue with vulnerability details
- Updates existing issues if already present
- Includes fix commands and recommendations
- Labels: `security`, `pip-audit`, `vulnerability`, `dependencies`

**When No Vulnerabilities** ✅:

- Closes any existing vulnerability issues
- Creates clean audit report (auto-closed)
- Labels: `security`, `pip-audit`, `clean`

## 📊 Example Reports

### Vulnerability Issue

```markdown
🚨 Security Audit: 3 vulnerabilities found in dependencies

## 🔍 Security Audit Summary
- **Vulnerabilities Found:** 3
- **Affected Packages:** 2
- **Scan Date:** 2025-09-19 08:00:00 UTC

## 🚨 Vulnerability Details
| Package | Version | Vulnerability ID | Fix Version |
|---------|---------|------------------|-------------|
| requests | 2.25.1 | PYSEC-2023-74 | >=2.31.0 |
| urllib3 | 1.26.5 | GHSA-v845-jxx5-vc9f | >=1.26.17 |

## 🔧 Manual Fix Commands
```bash
pip install requests>=2.31.0 urllib3>=1.26.17
pip-audit --fix  # Automatic fix (use with caution)
```

### Clean Audit Report

```markdown
✅ Weekly Security Audit: No vulnerabilities found

All dependencies scanned successfully against latest vulnerability databases.
No known security issues detected.
```

## ⚙️ Customization Options

### Change Scan Schedule

```yaml
schedule:
  # Daily at 2 AM UTC
  - cron: "0 2 * * *"
  
  # Twice weekly (Monday & Thursday)
  - cron: "0 8 * * 1,4"
```

### Scan Additional Files

```yaml
- name: Scan development dependencies
  run: |
    pip-audit -r requirements-dev.txt --format json --output dev-audit.json
```

### Ignore Specific Vulnerabilities

```yaml
- name: Run pip-audit with exclusions
  run: |
    pip-audit -r requirements.txt \
      --ignore-vuln CVE-2023-12345 \
      --ignore-vuln GHSA-xxxx-xxxx-xxxx
```

### Custom Python Version

```yaml
env:
  PYTHON_VERSION: "3.12"  # or 3.9, 3.10, 3.11, etc.
```

### Fail Workflow on Vulnerabilities

```yaml
# Add this to fail CI/CD on security issues
- name: Fail on vulnerabilities
  if: env.AUDIT_STATUS == 'vulnerabilities_found'
  run: exit 1
```

## 🛠️ Advanced Usage

### Local Development Workflow

```bash
# Install pip-audit locally
pip install pip-audit

# Scan your requirements
pip-audit -r requirements.txt

# Generate detailed report
pip-audit -r requirements.txt --desc --format json --output audit.json

# Attempt automatic fixes (review carefully)
pip-audit -r requirements.txt --fix --dry-run  # Preview changes
pip-audit -r requirements.txt --fix            # Apply fixes
```

### Integration with Pre-commit

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/pypa/pip-audit
    rev: v2.6.1
    hooks:
      - id: pip-audit
```

### Docker Integration

```dockerfile
# Add to your Dockerfile
RUN pip install pip-audit
RUN pip-audit -r requirements.txt --desc
```

## 🔍 Troubleshooting

### Common Issues

**❌ Workflow permissions error**

```markdown
Error: Resource not accessible by integration
```

**Solution**: Enable Issues write permission in Settings → Actions → General

**❌ No requirements.txt found**

```markdown
ERROR: File not found: requirements.txt
```

**Solution**: Ensure `requirements.txt` exists in repository root

**❌ pip-audit installation fails**

```markdown
ERROR: Could not install packages due to an EnvironmentError
```

**Solution**: Check network connectivity or use alternative installation method

### Debug Mode

Add verbose logging:

```yaml
- name: Debug pip-audit
  run: |
    pip-audit -r requirements.txt --verbose --format json
```

### View Workflow Logs

1. Go to **Actions** tab
2. Click on the failed workflow run
3. Expand the failed step to see detailed logs

## 📚 Additional Resources

- **[pip-audit Documentation](https://github.com/pypa/pip-audit)** - Official tool documentation
- **[GitHub Actions Security](https://docs.github.com/en/actions/security-guides)** - Security best practices
- **[Python Security](https://python.org/dev/security/)** - Python security resources
- **[PyPA Advisory Database](https://github.com/pypa/advisory-database)** - Vulnerability database
- **[OSV Database](https://osv.dev/)** - Open Source Vulnerabilities

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. Areas for improvement:

- 🔧 Additional workflow customizations
- 📊 Enhanced reporting features  
- 🔌 Integration with other security tools
- 📖 Documentation improvements
- 🐛 Bug fixes and optimizations

### Development Setup

```bash
git clone https://github.com/your-username/python-security-audit-recipe.git
cd python-security-audit-recipe

# Test the workflow locally (requires act)
act -j security-audit
```

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🏷️ Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history and updates.

## ⭐ Support

If this recipe helps secure your Python projects, please consider:

- ⭐ Starring this repository
- 🐛 Reporting issues or suggestions
- 🤝 Contributing improvements
- 📢 Sharing with other developers

## 🔗 Repository

- **GitHub**: [https://github.com/trivedi-vatsal/python-security-audit-recipe](https://github.com/trivedi-vatsal/python-security-audit-recipe)
- **Issues**: [Report bugs or request features](https://github.com/trivedi-vatsal/python-security-audit-recipe/issues)
- **Discussions**: [Community discussions](https://github.com/trivedi-vatsal/python-security-audit-recipe/discussions)

---

**Made with ❤️ for the Python security community by [Vatsal Trivedi](https://github.com/trivedi-vatsal)**

*Keep your dependencies secure, one audit at a time! 🔐*
