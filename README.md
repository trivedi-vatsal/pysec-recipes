# Python Security Audit Recipe 🔐

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-enabled-blue.svg)](https://github.com/features/actions)
[![pip-audit](https://img.shields.io/badge/security-pip--audit-red.svg)](https://github.com/pypa/pip-audit)
[![Recipe](https://img.shields.io/badge/type-recipe-orange.svg)](https://github.com/trivedi-vatsal/pysec-recipes)
[![Documentation](https://img.shields.io/badge/docs-GitHub%20Pages-blue.svg)](https://trivedi-vatsal.github.io/pysec-recipes/)

> **The Ultimate Recipe for Python Security** 🚀

A **production-ready GitHub Actions recipe** that transforms any Python project into a security-first codebase. This recipe automatically scans your dependencies for vulnerabilities, creates intelligent GitHub issues, and keeps your team informed about security risks—all with zero configuration required.

**Why This Recipe?** Because security shouldn't be an afterthought. This recipe makes Python security auditing as simple as copying a file.

## 📖 **Complete Documentation**

🌟 **[View Full Documentation](https://trivedi-vatsal.github.io/pysec-recipes/)** - Comprehensive guides, examples, and tutorials

### Quick Navigation

| Section | Description |
|---------|-------------|
| 🚀 [**Getting Started**](https://trivedi-vatsal.github.io/pysec-recipes/getting-started/) | Quick overview and setup guide |
| 💻 [**Installation**](https://trivedi-vatsal.github.io/pysec-recipes/installation/) | Step-by-step installation instructions |
| ⚙️ [**Configuration**](https://trivedi-vatsal.github.io/pysec-recipes/configuration/) | Customize workflows for your needs |
| 🔄 [**Workflow Guide**](https://trivedi-vatsal.github.io/pysec-recipes/workflow/) | Understand how the automation works |
| 📋 [**Examples**](https://trivedi-vatsal.github.io/pysec-recipes/examples/) | Real-world usage examples |
| 🎫 [**Issue Templates**](https://trivedi-vatsal.github.io/pysec-recipes/issue-templates/) | Automated issue management |
| ❓ [**FAQs**](https://trivedi-vatsal.github.io/pysec-recipes/faqs/) | Common questions and troubleshooting |

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

> 📖 **[Full Installation Guide](https://trivedi-vatsal.github.io/pysec-recipes/installation/)** - Complete setup instructions with troubleshooting

### Option 1: Basic Security Audit Workflow

1. **Create the workflow directory**:
   ```bash
   mkdir -p .github/workflows
   ```

2. **Copy the main workflow**:
   ```bash
   curl -o .github/workflows/security-audit.yml \
     https://raw.githubusercontent.com/trivedi-vatsal/pysec-recipes/main/.github/workflows/security-audit.yml
   ```

3. **Commit and push**:
   ```bash
   git add .github/workflows/security-audit.yml
   git commit -m "Add security audit workflow"
   git push
   ```

### Option 2: Complete Setup with Sample Workflow

Include the sample requirements scanner we just created:

```bash
# Create directories
mkdir -p .github/workflows .github/ISSUE_TEMPLATE

# Copy main workflow
curl -o .github/workflows/security-audit.yml \
  https://raw.githubusercontent.com/trivedi-vatsal/pysec-recipes/main/.github/workflows/security-audit.yml

# Copy sample workflow
curl -o .github/workflows/sample-security-audit.yml \
  https://raw.githubusercontent.com/trivedi-vatsal/pysec-recipes/main/.github/workflows/sample-security-audit.yml

# Copy issue templates
curl -o .github/ISSUE_TEMPLATE/security-vulnerability-report.md \
  https://raw.githubusercontent.com/trivedi-vatsal/pysec-recipes/main/.github/ISSUE_TEMPLATE/security-vulnerability-report.md

curl -o .github/ISSUE_TEMPLATE/clean-security-audit-report.md \
  https://raw.githubusercontent.com/trivedi-vatsal/pysec-recipes/main/.github/ISSUE_TEMPLATE/clean-security-audit-report.md
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

## 📊 Recipe Examples

> 📖 **[Complete Examples Guide](https://trivedi-vatsal.github.io/pysec-recipes/examples/)** - Real-world usage scenarios and configurations

### Available Example Workflows

| Example | Description | Use Case |
|---------|-------------|----------|
| 🔧 [**Basic Example**](https://trivedi-vatsal.github.io/pysec-recipes/examples/basic/) | Simple single-file security audit | Small projects, getting started |
| 🌍 [**Multi-Environment**](https://trivedi-vatsal.github.io/pysec-recipes/examples/multi-environment/) | Scan dev, test, prod requirements | Complex projects with multiple environments |
| 🐍 [**Django Project**](https://trivedi-vatsal.github.io/pysec-recipes/examples/django/) | Django-specific security scanning | Web applications using Django |
| ⚡ [**FastAPI Project**](https://trivedi-vatsal.github.io/pysec-recipes/examples/fastapi/) | FastAPI security workflows | Modern API development |
| 📦 [**Monorepo**](https://trivedi-vatsal.github.io/pysec-recipes/examples/monorepo/) | Multiple projects in one repository | Enterprise monorepo setups |
| 🧪 [**Sample Scanner**](sample/) | Demo workflow for sample dependencies | Testing and learning |

### 🧪 **Try the Sample Workflow**

We've included a sample security audit workflow that scans the example dependencies in `sample/requirements.txt`. This is perfect for:

- 🎯 **Learning** how the security workflows operate
- 🧪 **Testing** the setup in your repository  
- 📊 **Demonstrating** security scanning to your team
- 🔍 **Understanding** the audit reports and issue creation

**The sample workflow includes:**
- Multiple security tools: `pip-audit`, `safety`, and `bandit`
- Comprehensive reporting in JSON, Markdown, and text formats
- Automated GitHub issue creation for vulnerabilities
- Daily scheduled scans with manual trigger support
- Pull request integration with status comments

**Quick test:**
1. The workflow file is already in `.github/workflows/sample-security-audit.yml`
2. Go to **Actions** → **Sample Requirements Security Audit**
3. Click **Run workflow** to see it in action
4. Review the generated reports and issues

### 🚨 When Vulnerabilities Are Found

> 📖 **[Complete Issue Examples](https://trivedi-vatsal.github.io/pysec-recipes/issue-templates/)** - Detailed issue templates and examples

The recipe automatically creates a GitHub issue with:
- � **Vulnerability summary** with affected packages and severity
- 🛠️ **Fix commands** for automatic and manual remediation  
- 📊 **Detailed reports** with links to security databases
- 📋 **Next steps** with testing and update guidance

### ✅ When Everything Is Clean

Creates a clean audit report confirming:
- ✅ No vulnerabilities detected in current dependencies
- � Security recommendations and best practices
- � Confirmation of regular monitoring schedule

**Example reports and templates available in the [documentation](https://trivedi-vatsal.github.io/pysec-recipes/issue-templates/).**

## ⚙️ Customizing Your Recipe

> � **[Complete Configuration Guide](https://trivedi-vatsal.github.io/pysec-recipes/configuration/)** - Detailed customization options and examples

### Quick Customization Examples

| Customization | Documentation Link |
|---------------|-------------------|
| � **Change Scan Schedule** | [Scheduling Guide](https://trivedi-vatsal.github.io/pysec-recipes/configuration/#scheduling) |
| 📁 **Scan Multiple Files** | [Multi-file Setup](https://trivedi-vatsal.github.io/pysec-recipes/configuration/#multiple-files) |
| 🚫 **Ignore Vulnerabilities** | [Exclusion Patterns](https://trivedi-vatsal.github.io/pysec-recipes/configuration/#exclusions) |
| 🐍 **Python Version Control** | [Environment Setup](https://trivedi-vatsal.github.io/pysec-recipes/configuration/#python-versions) |
| 🚨 **CI/CD Integration** | [Build Failures](https://trivedi-vatsal.github.io/pysec-recipes/configuration/#cicd-integration) |
| 🔄 **Advanced Techniques** | [Advanced Usage](https://trivedi-vatsal.github.io/pysec-recipes/configuration/#advanced) |

## � Recipe Troubleshooting

> 📖 **[Complete Troubleshooting Guide](https://trivedi-vatsal.github.io/pysec-recipes/faqs/)** - Detailed solutions and debugging help

### � **Common Issues & Quick Fixes**

| Issue | Quick Solution |
|-------|----------------|
| ❌ Workflow permissions error | Settings → Actions → General → "Read and write permissions" |
| ❌ No requirements.txt found | Ensure `requirements.txt` exists in repository root |
| ❌ pip-audit installation fails | Check network connectivity or GitHub Actions status |
| ❌ Workflow not triggering | Verify GitHub Actions is enabled in repository settings |

### 🆘 **Need More Help?**

- **📖 [Full FAQ & Troubleshooting](https://trivedi-vatsal.github.io/pysec-recipes/faqs/)** - Comprehensive solutions
- **🐛 [Report Issues](https://github.com/trivedi-vatsal/pysec-recipes/issues)** - Bug reports and feature requests
- **💬 [Community Discussions](https://github.com/trivedi-vatsal/pysec-recipes/discussions)** - Get help from the community

## 📚 Additional Resources

> 📖 **[Complete Resource Library](https://trivedi-vatsal.github.io/pysec-recipes/)** - Links to all security tools and guides

**Quick Links:**
- **[pip-audit Documentation](https://github.com/pypa/pip-audit)** | **[GitHub Actions Security](https://docs.github.com/en/actions/security-guides)** | **[Python Security](https://python.org/dev/security/)**

## 🤝 Contributing

> 📖 **[Contributing Guide](https://trivedi-vatsal.github.io/pysec-recipes/contributing/)** - Full development setup and contribution guidelines

Contributions welcome! Areas for improvement: workflow customizations, reporting features, security tool integrations, documentation, and bug fixes.

## 📜 License & Changelog

- **License**: [MIT License](LICENSE) - see LICENSE file for details
- **Changes**: [CHANGELOG.md](CHANGELOG.md) - version history and updates

## 🚀 Ready to Secure Your Python Project?

### **Get Started in 30 Seconds**

```bash
# One command to secure your project
curl -sSL https://raw.githubusercontent.com/trivedi-vatsal/pysec-recipes/main/setup.py | python3
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

## 🔗 Connect & Learn More

### 📖 **Documentation & Resources**

- **🌟 [Complete Documentation](https://trivedi-vatsal.github.io/pysec-recipes/)** - Full guides and tutorials
- **📋 [Examples Library](https://trivedi-vatsal.github.io/pysec-recipes/examples/)** - Real-world usage scenarios
- **❓ [FAQ & Troubleshooting](https://trivedi-vatsal.github.io/pysec-recipes/faqs/)** - Common questions and solutions
- **⚙️ [Configuration Guide](https://trivedi-vatsal.github.io/pysec-recipes/configuration/)** - Customize for your needs

### 🤝 **Community & Support**

- **🐛 [Issues](https://github.com/trivedi-vatsal/pysec-recipes/issues)** - Report bugs or request features
- **💬 [Discussions](https://github.com/trivedi-vatsal/pysec-recipes/discussions)** - Community discussions and help
- **📧 [Contact](https://github.com/trivedi-vatsal)** - Reach out to the maintainer

### 🌟 **Join the Security-First Movement**

- ⭐ **Star this repository** to show your support
- 🔀 **Fork and contribute** to make Python security better
- 📢 **Share with your team** and help others secure their code
- 💬 **Join discussions** to learn and help the community

---

## Made with ❤️ for the Python Security Community

Transform your Python projects into security-first codebases with this powerful recipe! 🔐

[![GitHub stars](https://img.shields.io/github/stars/trivedi-vatsal/pysec-recipes?style=social)](https://github.com/trivedi-vatsal/pysec-recipes)
[![GitHub forks](https://img.shields.io/github/forks/trivedi-vatsal/pysec-recipes?style=social)](https://github.com/trivedi-vatsal/pysec-recipes)
[![GitHub watchers](https://img.shields.io/github/watchers/trivedi-vatsal/pysec-recipes?style=social)](https://github.com/trivedi-vatsal/pysec-recipes)
