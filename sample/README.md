# Multi-Environment Security Audit Recipe 🏢

This directory contains the **Enterprise Recipe** for Python Security Audit - a powerful multi-environment security scanning solution that audits multiple requirements files in parallel.

## 🎯 What This Recipe Does

The Multi-Environment Security Audit Recipe automatically scans different environment configurations (base, development, production, testing) and provides comprehensive security coverage across your entire project.

### Key Features

- ✅ **Parallel Environment Scanning** - Audits all environments simultaneously
- ✅ **Matrix Strategy** - Efficient parallel execution across environments
- ✅ **Environment-Specific Reports** - Separate audit results for each environment
- ✅ **Flexible Requirements Structure** - Works with any requirements file organization
- ✅ **Comprehensive Coverage** - Ensures no environment is left unsecured

## 📁 Repository Structure

This recipe expects the following structure:

```
your-project/
├── requirements/
│   ├── base.txt           # Common dependencies
│   ├── development.txt    # Development-specific dependencies
│   ├── production.txt     # Production-specific dependencies
│   └── testing.txt        # Testing-specific dependencies
├── .github/workflows/
│   └── multi-environment-audit.yml
└── [your project files]
```

## 🚀 Quick Setup

### 1. Download the Recipe

```bash
# Download the multi-environment recipe
curl -O https://raw.githubusercontent.com/trivedi-vatsal/python-security-audit-recipe/main/sample/multi-environment-audit.yml

# Move to your workflows directory
mv multi-environment-audit.yml .github/workflows/security-audit.yml
```

### 2. Create Requirements Structure

Create your requirements files:

```bash
# Create requirements directory
mkdir -p requirements

# Create environment-specific requirements files
touch requirements/base.txt
touch requirements/development.txt
touch requirements/production.txt
touch requirements/testing.txt
```

### 3. Example Requirements Files

**requirements/base.txt** (Common dependencies):
```txt
requests>=2.31.0
flask>=2.3.0
click>=8.1.0
```

**requirements/development.txt** (Development tools):
```txt
-r base.txt
pytest>=7.4.0
black>=23.0.0
flake8>=6.0.0
```

**requirements/production.txt** (Production dependencies):
```txt
-r base.txt
gunicorn>=21.0.0
whitenoise>=6.5.0
```

**requirements/testing.txt** (Testing dependencies):
```txt
-r base.txt
pytest>=7.4.0
pytest-cov>=4.1.0
```

## 🔧 How the Recipe Works

### Matrix Strategy

The recipe uses GitHub Actions matrix strategy to run parallel audits:

```yaml
strategy:
  matrix:
    environment: [base, development, production, testing]
    include:
      - environment: base
        requirements: requirements/base.txt
      - environment: development
        requirements: requirements/development.txt
      - environment: production
        requirements: requirements/production.txt
      - environment: testing
        requirements: requirements/testing.txt
  fail-fast: false
```

### Parallel Execution

Each environment runs in parallel, making the audit process efficient:

- **Base Environment** - Scans common dependencies
- **Development Environment** - Scans dev tools and base dependencies
- **Production Environment** - Scans production-specific dependencies
- **Testing Environment** - Scans testing frameworks and base dependencies

### Environment-Specific Reports

Each environment generates its own audit report:

- `audit-outputs/audit-base.json` - Base environment vulnerabilities
- `audit-outputs/audit-development.json` - Development environment vulnerabilities
- `audit-outputs/audit-production.json` - Production environment vulnerabilities
- `audit-outputs/audit-testing.json` - Testing environment vulnerabilities

## ⚙️ Customization Options

### 1. Add More Environments

To add more environments, update the matrix strategy:

```yaml
strategy:
  matrix:
    environment: [base, development, staging, production, testing, security]
    include:
      - environment: base
        requirements: requirements/base.txt
      - environment: development
        requirements: requirements/development.txt
      - environment: staging
        requirements: requirements/staging.txt
      - environment: production
        requirements: requirements/production.txt
      - environment: testing
        requirements: requirements/testing.txt
      - environment: security
        requirements: requirements/security.txt
```

### 2. Change Scan Schedule

Modify the schedule in the workflow:

```yaml
on:
  schedule:
    - cron: "0 8 * * 1"  # Weekly on Monday at 8 AM UTC
    # - cron: "0 2 * * *"  # Daily at 2 AM UTC
    # - cron: "0 8 * * 1,4"  # Monday and Thursday
```

### 3. Custom Python Version

Update the Python version:

```yaml
env:
  PYTHON_VERSION: "3.12"  # Change to your preferred version
```

### 4. Ignore Specific Vulnerabilities

Add exclusions to the audit command:

```yaml
- name: Run security audit for ${{ matrix.environment }}
  run: |
    pip-audit -r "${{ matrix.requirements }}" \
      --ignore-vuln CVE-2023-12345 \
      --ignore-vuln GHSA-xxxx-xxxx-xxxx \
      --format json \
      --output "audit-outputs/audit-${{ matrix.environment }}.json" || true
```

## 📊 Recipe Output

### What You Get

After running the recipe, you'll have:

1. **Environment-Specific Artifacts** - Separate audit results for each environment
2. **Comprehensive Coverage** - All environments scanned in parallel
3. **Detailed Reports** - JSON and Markdown formats for each environment
4. **Vulnerability Tracking** - Clear visibility into which environments have issues

### Sample Output Structure

```
audit-outputs/
├── audit-base.json          # Base environment vulnerabilities
├── audit-base.md            # Human-readable base report
├── audit-development.json   # Development environment vulnerabilities
├── audit-development.md     # Human-readable dev report
├── audit-production.json    # Production environment vulnerabilities
├── audit-production.md      # Human-readable prod report
├── audit-testing.json       # Testing environment vulnerabilities
└── audit-testing.md         # Human-readable test report
```

## 🚀 Getting Started

### 1. Download and Setup

```bash
# Download the multi-environment recipe
curl -O https://raw.githubusercontent.com/trivedi-vatsal/python-security-audit-recipe/main/sample/multi-environment-audit.yml

# Create workflows directory
mkdir -p .github/workflows

# Move the recipe to workflows directory
mv multi-environment-audit.yml .github/workflows/security-audit.yml
```

### 2. Create Your Requirements Structure

```bash
# Create requirements directory
mkdir -p requirements

# Create your environment-specific requirements files
echo "requests>=2.31.0" > requirements/base.txt
echo "-r base.txt" > requirements/development.txt
echo "pytest>=7.4.0" >> requirements/development.txt
echo "-r base.txt" > requirements/production.txt
echo "gunicorn>=21.0.0" >> requirements/production.txt
echo "-r base.txt" > requirements/testing.txt
echo "pytest>=7.4.0" >> requirements/testing.txt
```

### 3. Commit and Push

```bash
git add .
git commit -m "Add multi-environment security audit recipe"
git push
```

### 4. Test the Recipe

1. Go to **Actions** tab in your GitHub repository
2. Select **"Multi-Environment Security Audit"**
3. Click **"Run workflow"** → **"Run workflow"**
4. Watch all environments scan in parallel! ✨

## 🎯 Perfect For

- **Enterprise Projects** with multiple environments
- **Complex Applications** with different dependency sets
- **Teams** that need environment-specific security visibility
- **Projects** with separate dev/staging/prod configurations
- **Organizations** requiring comprehensive security coverage

## 🔗 Related Resources

- **[Main Recipe](../README.md)** - Basic single-environment recipe
- **[Documentation](../docs/)** - Complete documentation
- **[Getting Started](../docs/getting-started.md)** - Step-by-step setup guide
- **[Configuration](../docs/configuration.md)** - Advanced customization options

---

**Ready to secure all your environments?** Download the Multi-Environment Security Audit Recipe and get comprehensive security coverage across your entire project! 🚀
