# Changelog

All notable changes to the Python Security Audit Recipe will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2025-09-20

### Added

- **Enhanced Documentation Structure**: Complete MkDocs-based documentation with comprehensive guides
- **Recipe Examples**: Detailed examples for Django, FastAPI, basic, multi-environment, and monorepo setups
- **Configuration Guide**: Advanced configuration options for customizing security audit workflows
- **Workflow Documentation**: Complete workflow code with detailed explanations and best practices
- **Getting Started Guide**: Step-by-step guide for new users with prerequisites and setup instructions
- **Installation Guide**: Comprehensive installation documentation for different project types
- **Issue Templates Documentation**: Detailed guide for GitHub issue templates and management
- **Project Infrastructure**: Enhanced gitignore and requirements for documentation builds

### Changed

- **Renamed Documentation File**: `LOCAL_DEVELOPMENT.md` → `MKDOCS.md` for better clarity
- **Enhanced MkDocs Configuration**: Improved theme, navigation, and plugin configuration
- **Improved README**: Enhanced with better structure, clearer instructions, and more comprehensive feature descriptions
- **Better Project Structure**: More organized documentation hierarchy with logical grouping

### Documentation Additions

- **Recipe Examples**: Five detailed examples covering different project types and use cases
- **Configuration Management**: Advanced configuration options for different environments
- **Workflow Mechanics**: Deep dive into GitHub Actions workflow components
- **Issue Templates**: Complete guide for managing security notification issues
- **Getting Started**: Comprehensive onboarding experience for new users

### Files Added

- `docs/configuration.md` - Advanced configuration guide
- `docs/examples.md` - Recipe examples overview
- `docs/examples/basic.md` - Basic project example
- `docs/examples/django.md` - Django application example
- `docs/examples/fastapi.md` - FastAPI application example
- `docs/examples/monorepo.md` - Monorepo setup example
- `docs/examples/multi-environment.md` - Multi-environment configuration
- `docs/getting-started.md` - Getting started guide
- `docs/workflow.md` - Complete workflow documentation
- `.gitignore` - Comprehensive gitignore for Python projects
- `requirements-docs.txt` - Documentation build dependencies

### Infrastructure Improvements

- **MkDocs Integration**: Full documentation site generation with Material theme
- **Enhanced Navigation**: Logical documentation structure with progress tracking
- **Code Highlighting**: Improved syntax highlighting for code examples
- **Documentation Build System**: Streamlined documentation generation process

## [1.0.0] - 2025-09-19

### Added

- GitHub Actions workflow for automated security auditing using `pip-audit`
- Smart issue management that creates, updates, and closes security issues
- Support for multiple output formats (JSON, Markdown, text)
- Weekly scheduled scans with manual trigger option
- Artifact storage with 90-day retention
- Issue templates for vulnerability and clean audit reports
- Comprehensive documentation and setup guide
- MIT license for open-source distribution
- Initial release of Python Security Audit Recipe
- Comprehensive README with setup instructions
- Automated setup script (`setup.py`)
- Example configurations for various scenarios
- Multi-environment workflow example

### Features

- **Automated Scanning**: Weekly scheduled scans + manual triggers
- **Multiple Report Formats**: JSON, Markdown, and text outputs
- **Smart Issue Management**: Creates, updates, and closes security issues automatically
- **Artifact Storage**: 90-day retention of detailed audit results
- **Comprehensive Coverage**: Scans `requirements.txt` and dependency trees
- **Zero Configuration**: Works out-of-the-box with sensible defaults
- **Highly Customizable**: Easy to adapt for different project needs

### Workflow Capabilities

- Scans Python dependencies for known security vulnerabilities
- Automatically creates GitHub issues when vulnerabilities are found
- Updates existing issues with new scan results
- Closes vulnerability issues when problems are resolved
- Generates clean audit reports for vulnerability-free scans
- Fails CI/CD pipeline on security issues (configurable)
- Supports custom Python versions and branch configurations

### Documentation

- Complete setup instructions in README.md
- Automated setup script for easy adoption
- Example configurations for advanced use cases
- Troubleshooting guide and best practices
- Integration examples for CI/CD pipelines

### Security

- Uses latest `pip-audit` tool for vulnerability detection
- Leverages multiple vulnerability databases (PyPI, OSV, etc.)
- Provides detailed remediation instructions
- Supports vulnerability exclusions for false positives
- Implements secure GitHub Actions practices

---

For more details about each release, see the [GitHub Releases](https://github.com/trivedi-vatsal/pysec-recipes/releases) page.
