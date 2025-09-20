# 🐍 Python Security Audit Recipe 🔐

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-enabled-blue.svg)](https://github.com/features/actions)
[![pip-audit](https://img.shields.io/badge/security-pip--audit-red.svg)](https://github.com/pypa/pip-audit)
[![Recipe](https://img.shields.io/badge/type-recipe-orange.svg)](https://github.com/trivedi-vatsal/pysec-recipes)
[![Documentation](https://img.shields.io/badge/docs-GitHub%20Pages-blue.svg)](https://trivedi-vatsal.github.io/pysec-recipes/)

> **Automated, Zero-Config Security for Your Python Projects** 🚀

This **production-ready GitHub Actions recipe** is your secret weapon for a security-first codebase. It automatically scans your project's dependencies for vulnerabilities, creates intelligent GitHub issues, and keeps your team in the loop—all with a **one-command setup**.

## 🚀 Why This Recipe?

Security shouldn't be an afterthought. Manual security audits are slow, error-prone, and often forgotten. This recipe solves that by making automated security as simple as copying a file.

### What You Get Out of the Box

* **🛡️ Instant Security:** Set up in less than a minute. Just copy, paste, and commit.
* **🧠 Intelligent Automation:** Automatically creates, updates, and closes security issues.
* **🚨 Real-Time Alerts:** Get notified the moment a vulnerability is found.
* **👥 Team Collaboration:** Shared visibility and a clear action plan for every security risk.

## 📖 Quick Start: Secure Your Project in 30 Seconds

Getting started is as easy as running a single command in your project's root directory.

```bash
# One command to add security automation to your project
curl -sSL https://raw.githubusercontent.com/trivedi-vatsal/pysec-recipes/main/setup.py | python3
```

This command automatically creates a new workflow file at `.github/workflows/security-audit.yml` and essential issue templates, instantly securing your project.

> 📖 **[Full Installation Guide](https://trivedi-vatsal.github.io/pysec-recipes/installation/)** - Detailed steps and troubleshooting.

## 🎯 Features at a Glance

### 🚀 **Instant & Effortless**

* **Zero Configuration:** Works right out of the box with sensible defaults.
* **Zero Maintenance:** Runs automatically on a schedule, with no manual upkeep required.
* **Comprehensive:** Scans `requirements.txt` and a full dependency tree.

### 🧠 **Smart & Actionable**

* **Smart Issue Management:** When a vulnerability is found, the recipe creates a detailed GitHub issue with fix instructions. It also closes issues when a vulnerability is resolved.
* **Rich Reporting:** Every scan generates detailed JSON, Markdown, and text reports for easy review.
* **Scheduled & On-Demand:** Scans run automatically every week and can be triggered manually.
* **Artifact Storage:** Stores audit reports for 90 days for full audit trail and compliance.

### 🛡️ **Enterprise-Grade**

* **Multiple Databases:** Leverages PyPI Advisory, OSV, and Python Packaging Advisory for robust coverage.
* **Fix Guidance:** Each issue includes direct `pip-audit` fix commands.
* **CI/CD Integration:** Can be configured to fail builds on critical vulnerabilities, ensuring no risky code gets deployed.

## 📋 What the Recipe Adds

Running the quick start command creates the following structure in your repository:

```markdown
your-repo/
├── .github/
│   ├── workflows/
│   │   └── security-audit.yml           # The main security workflow
│   └── ISSUE_TEMPLATE/
│       ├── security-vulnerability-report.md # Template for vulnerability issues
│       └── clean-security-audit-report.md   # Template for clean reports
├── requirements.txt                     # Your project's dependencies
└── [your project files]
```

### How the Workflow Works

The `security-audit.yml` workflow is designed to run automatically on a weekly schedule, on every push to the main branch, or when triggered manually. It does the following:

1. Sets up a Python environment and `pip-audit`.
2. Scans your `requirements.txt` file for known vulnerabilities.
3. Generates easy-to-read reports.
4. Creates, updates, or closes a GitHub issue based on the scan results.
5. Uploads the detailed reports as artifacts for long-term storage.

## 📊 Examples & Use Cases

This recipe is versatile and can be customized for many project types.

| Example | Description | Use Case |
|---------|-------------|----------|
| 🔧 **Basic Example** | A single-file security audit. | Small projects, quick setup. |
| 🌍 **Multi-Environment** | Scans separate `dev`, `test`, and `prod` requirements files. | Complex projects with different dependencies. |
| 🐍 **Django Project** | Specifically tailored for Django applications. | Securing web applications. |
| 📦 **Monorepo** | Audits multiple projects within a single repository. | Enterprise setups. |

> 📖 **[View All Examples](https://trivedi-vatsal.github.io/pysec-recipes/examples/)** - Explore configurations for different project types.

## 💡 Troubleshooting & Support

Have questions or need help? The documentation is here for you.

* **📖 [Full Documentation](https://trivedi-vatsal.github.io/pysec-recipes/)** - Comprehensive guides and explanations.
* **❓ [FAQs & Troubleshooting](https://trivedi-vatsal.github.io/pysec-recipes/faqs/)** - Find answers to common issues.
* **🐛 [Report an Issue](https://github.com/trivedi-vatsal/pysec-recipes/issues)** - Report bugs or request features.

This recipe is a open effort. Your contributions are welcome\! If you have ideas for new features, better reporting, or bug fixes

## Made with ❤️ for the Python Security

Star this repository to show your support and help others discover it. Let's make Python security simple and accessible for everyone

[![GitHub stars](https://img.shields.io/github/stars/trivedi-vatsal/pysec-recipes?style=social)](https://github.com/trivedi-vatsal/pysec-recipes)
[![GitHub forks](https://img.shields.io/github/forks/trivedi-vatsal/pysec-recipes?style=social)](https://github.com/trivedi-vatsal/pysec-recipes)
[![GitHub watchers](https://img.shields.io/github/watchers/trivedi-vatsal/pysec-recipes?style=social)](https://github.com/trivedi-vatsal/pysec-recipes)
