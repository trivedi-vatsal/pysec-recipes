# Python Security Audit Recipe 🔐

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-enabled-blue.svg)](https://github.com/features/actions)
[![pip-audit](https://img.shields.io/badge/security-pip--audit-red.svg)](https://github.com/pypa/pip-audit)
[![Recipe](https://img.shields.io/badge/type-recipe-orange.svg)](https://github.com/trivedi-vatsal/python-security-audit-recipe)

> **The Ultimate Recipe for Python Security** 🚀

A **production-ready GitHub Actions recipe** that transforms any Python project into a security-first codebase. This recipe automatically scans your dependencies for vulnerabilities, creates intelligent GitHub issues, and keeps your team informed about security risks—all with zero configuration required.

**Why This Recipe?** Because security shouldn't be an afterthought. This recipe makes Python security auditing as simple as copying a file.

## 🎯 What This Recipe Gives You

### 🚀 **Instant Security** (30 seconds setup)

- **One-command setup**: Copy, paste, commit—you're secure
- **Zero maintenance**: Runs automatically, updates itself
- **Works everywhere**: Any Python project, any size

### 🧠 **Intelligent Automation**

- **🎫 Smart Issue Management**: Creates, updates, and closes security issues automatically
- **📊 Rich Reporting**: JSON, Markdown, and text outputs for every scan
- **🔄 Scheduled & On-Demand**: Weekly scans + manual triggers when you need them
- **📁 Artifact Storage**: 90-day retention of detailed audit results

### 🛡️ **Enterprise-Grade Security**

- **Comprehensive Coverage**: Scans `requirements.txt` and entire dependency trees
- **Multiple Databases**: PyPI Advisory, OSV, Python Packaging Advisory
- **Real-time Alerts**: Immediate notification when vulnerabilities are found
- **Fix Guidance**: Automatic fix commands and remediation steps

### ⚡ **Developer-Friendly**

- **Zero Configuration**: Works out-of-the-box with sensible defaults
- **Highly Customizable**: Easy to adapt for different project needs
- **CI/CD Integration**: Fails builds on critical vulnerabilities (optional)
- **Team Collaboration**: Shared security visibility across your organization

## 🚀 Quick Start (30 Seconds)

### Option 1: One-Command Setup (Recommended)

```bash
# Run the automated setup script
curl -sSL https://raw.githubusercontent.com/trivedi-vatsal/python-security-audit-recipe/main/setup.py | python3
```

### Option 2: Manual Setup

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

### 3. Customize (Optional)

Edit `.github/workflows/security-audit.yml` and update:

```yaml
# Change the default branch name if needed
branches: [main]  # or [master, develop, etc.]

# Adjust Python version
env:
  PYTHON_VERSION: "3.11"  # or your preferred version
```

### 4. Enable Permissions

Go to **Settings → Actions → General** and ensure:

- ✅ **Issues**: Write access to create/update security issues
- ✅ **Actions**: Enabled to run the workflow
- ✅ **Contents**: Read access to scan your repository

### 5. Test Your Recipe

1. Go to **Actions** tab in your GitHub repository
2. Select **Security Audit with pip-audit**
3. Click **Run workflow** → **Run workflow**
4. Watch the magic happen! ✨

**That's it!** Your Python project is now security-audited automatically.

## 🤔 Why This Recipe?

### The Problem

- **Manual security audits** are time-consuming and often forgotten
- **Security vulnerabilities** in dependencies can go unnoticed for months
- **Team coordination** on security issues is challenging
- **Compliance requirements** demand regular security assessments

### The Solution

This recipe solves all these problems with **one simple setup**:

| Before This Recipe | After This Recipe |
|-------------------|-------------------|
| ❌ Manual security checks | ✅ Automated weekly scans |
| ❌ Security issues go unnoticed | ✅ Instant GitHub issue creation |
| ❌ No team visibility | ✅ Shared security dashboard |
| ❌ Compliance headaches | ✅ Audit trail and reports |
| ❌ Complex setup | ✅ 30-second installation |

### Real-World Impact

- **🚨 Immediate Alerts**: Know about vulnerabilities within hours, not months
- **📈 Team Productivity**: Developers focus on features, not security maintenance
- **🛡️ Risk Reduction**: Catch vulnerabilities before they become security incidents
- **📊 Compliance Ready**: Automated reports for security audits and certifications

## 📋 What This Recipe Creates

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

## 📊 Recipe in Action

### 🚨 When Vulnerabilities Are Found

The recipe automatically creates a detailed GitHub issue:

```markdown
🚨 Security Audit: 3 vulnerabilities found in dependencies

## 🔍 Security Audit Summary
- Vulnerabilities Found: 3
- Affected Packages: 2
- Scan Date: 2025-09-19 08:00:00 UTC
- Repository: your-org/your-project
- Branch: main
- Commit: abc123def456

## 🚨 Vulnerability Details
| Package | Version | Vulnerability ID | Fix Version | Severity |
|---------|---------|------------------|-------------|----------|
| requests | 2.25.1 | PYSEC-2023-74 | >=2.31.0 | HIGH |
| urllib3 | 1.26.5 | GHSA-v845-jxx5-vc9f | >=1.26.17 | MEDIUM |
| urllib3 | 1.26.5 | CVE-2023-45803 | >=2.0.7 | HIGH |

## 🔧 Automatic Fix Commands
```bash
# Review the vulnerabilities
pip-audit -r requirements.txt

# Apply automatic fixes (use with caution)
pip-audit -r requirements.txt --fix

# Or update manually
pip install "requests>=2.31.0" "urllib3>=2.0.7"
```

## 📋 Next Steps

1. Review each vulnerability listed above
2. Update affected packages to the recommended fix versions
3. Test the application after updates
4. Consider using `pip-audit --fix` for automatic updates

---
*This issue was automatically generated by the Security Audit Recipe.*
*Workflow run: [View Details](https://github.com/your-org/your-project/actions/runs/123456)*

### ✅ When Everything Is Clean

The recipe creates a clean audit report:

```markdown
✅ Weekly Security Audit: No vulnerabilities found

## 🔍 Security Audit Summary
- **Status:** ✅ CLEAN - No vulnerabilities detected
- **Scan Date:** 2025-09-19 08:00:00 UTC
- **Dependencies Scanned:** 15 packages
- **Vulnerability Databases:** PyPI Advisory, OSV, Python Packaging Advisory

## 🛡️ Security Status
✅ All packages are up-to-date with security patches
✅ No known CVEs affecting current dependency versions
✅ Dependencies are from trusted sources

## 📈 Recommendations
Even though no vulnerabilities were found, consider these security best practices:
1. **Keep dependencies updated** - Regularly update to the latest stable versions
2. **Monitor security advisories** - Subscribe to security notifications
3. **Use dependency pinning** - Pin exact versions in production
4. **Regular audits** - This automated scan runs weekly

---
*This clean audit report was automatically generated by the Security Audit Recipe.*
```

## ⚙️ Customizing Your Recipe

### 🕐 **Change Scan Schedule**

```yaml
schedule:
  # Daily at 2 AM UTC
  - cron: "0 2 * * *"
  
  # Twice weekly (Monday & Thursday)
  - cron: "0 8 * * 1,4"
  
  # Monthly on first Monday
  - cron: "0 8 1-7 * 1"
```

### 📁 **Scan Additional Files**

```yaml
- name: Scan development dependencies
  run: |
    pip-audit -r requirements-dev.txt --format json --output dev-audit.json
    pip-audit -r requirements-test.txt --format json --output test-audit.json
```

### 🚫 **Ignore Specific Vulnerabilities**

```yaml
- name: Run pip-audit with exclusions
  run: |
    pip-audit -r requirements.txt \
      --ignore-vuln CVE-2023-12345 \
      --ignore-vuln GHSA-xxxx-xxxx-xxxx
```

### 🐍 **Custom Python Version**

```yaml
env:
  PYTHON_VERSION: "3.12"  # or 3.9, 3.10, 3.11, etc.
```

### 🚨 **Fail CI/CD on Vulnerabilities**

```yaml
# Add this to fail builds on security issues
- name: Fail on vulnerabilities
  if: env.AUDIT_STATUS == 'vulnerabilities_found'
  run: |
    echo "❌ Security vulnerabilities detected!"
    echo "Check the created issue for details and remediation steps."
    exit 1
```

## 🛠️ Advanced Recipe Techniques

### 🏠 **Local Development**

Test your recipe locally before committing:

```bash
# Install pip-audit locally
pip install pip-audit

# Scan your requirements
pip-audit -r requirements.txt

# Generate detailed report
pip-audit -r requirements.txt --desc --format json --output audit.json

# Test automatic fixes (review carefully)
pip-audit -r requirements.txt --fix --dry-run  # Preview changes
pip-audit -r requirements.txt --fix            # Apply fixes
```

### 🔄 **Pre-commit Integration**

Add security checks to every commit:

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/pypa/pip-audit
    rev: v2.6.1
    hooks:
      - id: pip-audit
        args: ['--desc', '--format=json']
```

### 🐳 **Docker Integration**

Secure your container builds:

```dockerfile
# Add to your Dockerfile
RUN pip install pip-audit
RUN pip-audit -r requirements.txt --desc

# Or as a separate security stage
FROM python:3.11 as security-check
COPY requirements.txt .
RUN pip install pip-audit
RUN pip-audit -r requirements.txt
```

### 📱 **Slack/Teams Notifications**

Get instant notifications when vulnerabilities are found:

```yaml
- name: Notify on Slack
  if: env.AUDIT_STATUS == 'vulnerabilities_found'
  uses: 8398a7/action-slack@v3
  with:
    status: failure
    text: "🚨 Security vulnerabilities found in ${{ github.repository }}"
  env:
    SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK }}
```

### 🔍 **Matrix Strategy**

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

## 🔍 Recipe Troubleshooting

### 🚨 **Common Issues & Solutions**

#### **❌ Workflow permissions error**

```markdown
Error: Resource not accessible by integration
```

**Solution**: Go to Settings → Actions → General → Workflow permissions → Select "Read and write permissions"

#### **❌ No requirements.txt found**

```markdown
ERROR: File not found: requirements.txt
```

**Solution**: Ensure `requirements.txt` exists in your repository root

#### **❌ pip-audit installation fails**

```markdown
ERROR: Could not install packages due to an EnvironmentError
```

**Solution**: Check network connectivity or use alternative installation method

#### **❌ Workflow not triggering**

**Solution**: Check that GitHub Actions is enabled in your repository settings

### 🐛 **Debug Mode**

Add verbose logging to your recipe:

```yaml
- name: Debug pip-audit
  run: |
    pip-audit -r requirements.txt --verbose --format json
```

### 📊 **View Workflow Logs**

1. Go to **Actions** tab in your repository
2. Click on the failed workflow run
3. Expand the failed step to see detailed logs
4. Check the "Security Audit" step for specific error messages

### 🆘 **Still Having Issues?**

- **Check the [Issues](https://github.com/trivedi-vatsal/python-security-audit-recipe/issues)** for known problems
- **Start a [Discussion](https://github.com/trivedi-vatsal/python-security-audit-recipe/discussions)** for help
- **Review the [Documentation](https://trivedi-vatsal.github.io/python-security-audit-recipe/)** for detailed guides

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
git clone https://github.com/trivedi-vatsal/python-security-audit-recipe.git
cd python-security-audit-recipe

# Test the workflow locally (requires act)
act -j security-audit
```

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🏷️ Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history and updates.

## 🚀 Ready to Secure Your Python Project?

### **Get Started in 30 Seconds**

```bash
# One command to secure your project
curl -sSL https://raw.githubusercontent.com/trivedi-vatsal/python-security-audit-recipe/main/setup.py | python3
```

### **Why Thousands of Developers Choose This Recipe**

- ✅ **Zero Configuration** - Works out of the box
- ✅ **Production Ready** - Used by teams worldwide
- ✅ **Actively Maintained** - Regular updates and improvements
- ✅ **Community Driven** - Open source and collaborative
- ✅ **Comprehensive** - Covers all Python security needs

### **Join the Security-First Community**

- ⭐ **Star this repository** to show your support
- 🐛 **Report issues** or suggest improvements
- 🤝 **Contribute** to make Python security better for everyone
- 📢 **Share** with your team and network
- 💬 **Join discussions** to learn and help others

## 🔗 Connect & Contribute

- **📖 Documentation**: [https://trivedi-vatsal.github.io/python-security-audit-recipe](https://trivedi-vatsal.github.io/python-security-audit-recipe)
- **🐛 Issues**: [Report bugs or request features](https://github.com/trivedi-vatsal/python-security-audit-recipe/issues)
- **💬 Discussions**: [Community discussions](https://github.com/trivedi-vatsal/python-security-audit-recipe/discussions)
- **📧 Contact**: [Vatsal Trivedi](https://github.com/trivedi-vatsal)

---

<div align="center">

**Made with ❤️ for the Python security community**

*Transform your Python projects into security-first codebases with this powerful recipe! 🔐*

[![GitHub stars](https://img.shields.io/github/stars/trivedi-vatsal/python-security-audit-recipe?style=social)](https://github.com/trivedi-vatsal/python-security-audit-recipe)
[![GitHub forks](https://img.shields.io/github/forks/trivedi-vatsal/python-security-audit-recipe?style=social)](https://github.com/trivedi-vatsal/python-security-audit-recipe)
[![GitHub watchers](https://img.shields.io/github/watchers/trivedi-vatsal/python-security-audit-recipe?style=social)](https://github.com/trivedi-vatsal/python-security-audit-recipe)

</div>
