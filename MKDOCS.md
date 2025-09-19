# MkDocs Guide - GitHub Pages Hosting

This guide will help you set up and run the MkDocs documentation site locally and deploy it automatically to GitHub Pages.

## Prerequisites

- Python 3.7 or higher
- Git
- GitHub account with repository access

## Local Development Setup

### 1. Clone the Repository

```bash
git clone https://github.com/trivedi-vatsal/python-security-audit-recipe.git
cd python-security-audit-recipe
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python -m venv docs-env

# Activate virtual environment
# On Windows:
.\docs-env\Scripts\Activate.ps1
# On macOS/Linux:
source docs-env/bin/activate
```

### 3. Install UV (Fast Python Package Manager)

```bash
# Install uv globally
pip install uv
```

### 4. Install Dependencies with UV

```bash
# Install documentation dependencies using uv
uv pip install --system -r requirements-docs.txt
```

### 5. Run Documentation Server

```bash
mkdocs serve
```

The documentation will be available at: `http://127.0.0.1:8000`

## GitHub Pages Automatic Deployment

The repository is configured for **automatic deployment** to GitHub Pages using GitHub Actions.

### How It Works

1. **GitHub Actions Workflow**: `.github/workflows/docs.yml` automatically builds and deploys docs
2. **Trigger**: Deployment happens on every push to `main` branch when docs files change
3. **Live Site**: Your docs are automatically published to GitHub Pages

### GitHub Pages Setup

#### 1. Enable GitHub Pages in Repository Settings

1. Go to your repository on GitHub
2. Click **Settings** tab
3. Scroll down to **Pages** section
4. Under **Source**, select **"GitHub Actions"**
5. Save the settings

#### 2. Automatic Deployment

The GitHub Actions workflow will automatically:

- Install Python and UV
- Install documentation dependencies with `uv pip install --system -r requirements-docs.txt`
- Build the documentation with `mkdocs build`
- Deploy to GitHub Pages

#### 3. Access Your Live Documentation

After setup, your documentation will be available at:

**<https://trivedi-vatsal.github.io/python-security-audit-recipe>**

## Development Commands

### Serve Documentation (with auto-reload)

```bash
mkdocs serve
```

### Build Documentation Locally

```bash
mkdocs build
```

### Build with Verbose Output (for debugging)

```bash
mkdocs serve --verbose
mkdocs build --verbose
```

### Manual GitHub Pages Deployment (Optional)

```bash
# Only if you want to deploy manually (not recommended)
mkdocs gh-deploy
```

## GitHub Actions Workflow Features

The `.github/workflows/docs.yml` includes:

- ✅ **UV Package Manager**: Fast dependency installation
- ✅ **Automatic Triggers**: Deploys on docs changes
- ✅ **Manual Triggers**: Can be run manually from Actions tab
- ✅ **Clean Builds**: Uses `mkdocs build --clean --strict`
- ✅ **GitHub Pages Integration**: Direct deployment to Pages

### Workflow Triggers

The documentation deploys automatically when:

- Changes are pushed to `main` branch
- Files in `docs/` folder are modified
- `mkdocs.yml` is updated
- `requirements-docs.txt` is changed
- The workflow file itself is modified

## Project Structure

```text
python-security-audit-recipe/
├── docs/                           # Documentation source files
│   ├── index.md                   # Home page
│   ├── workflow.md                # Complete workflow code
│   ├── configuration.md           # Configuration examples
│   └── examples.md                # Project examples
├── .github/                       # GitHub workflows and templates
│   ├── workflows/
│   │   ├── security-audit.yml     # Main security audit workflow
│   │   └── docs.yml               # Documentation deployment workflow
│   └── ISSUE_TEMPLATE/
│       ├── security-vulnerability-report.md
│       └── clean-security-audit-report.md
├── examples/                      # Example configurations
├── docs-env/                      # Virtual environment (ignored by git)
├── mkdocs.yml                     # MkDocs configuration
├── requirements-docs.txt          # Documentation dependencies
└── MKDOCS.md                      # This file
```

## GitHub Pages Development Workflow

### Making Changes

1. **Edit Documentation**: Modify files in the `docs/` folder
2. **Test Locally**: Run `mkdocs serve` to preview changes
3. **Auto-reload**: Changes automatically appear in the browser
4. **Test Build**: Run `mkdocs build --clean --strict` to ensure no errors
5. **Commit & Push**: Push to `main` branch - GitHub Actions will auto-deploy

### Automatic Deployment Process

When you push changes to the main branch:

1. **GitHub Actions Triggers**: `.github/workflows/docs.yml` runs automatically
2. **Build Process**: UV installs dependencies and MkDocs builds the site
3. **Deploy to Pages**: Site is automatically published to GitHub Pages
4. **Live in Minutes**: Your changes are live at the GitHub Pages URL

## Local Development Troubleshooting

### Issue: Port already in use

```bash
# Kill existing MkDocs process
# On Windows:
taskkill /f /im python.exe
# On macOS/Linux:
pkill -f "mkdocs serve"

# Or use a different port:
mkdocs serve --dev-addr=127.0.0.1:8001
```

### Issue: Virtual environment not activated

```bash
# Make sure you see (docs-env) in your terminal prompt
# If not, activate it:
# Windows:
.\docs-env\Scripts\Activate.ps1
# macOS/Linux:
source docs-env/bin/activate
```

### Issue: Dependencies not installed

```bash
# Ensure you're in the virtual environment and run:
uv pip install --system -r requirements-docs.txt
```

## MkDocs Configuration

The site is configured in `mkdocs.yml`:

- **Theme**: Material Design with dark theme
- **Features**: Code copy, syntax highlighting, navigation tabs
- **Plugins**: Search, git revision dates, minification
- **Navigation**: Organized sections for easy browsing

## Links

- **Local Development**: <http://127.0.0.1:8000>
- **Live GitHub Pages Site**: <https://trivedi-vatsal.github.io/python-security-audit-recipe>
- **Repository**: <https://github.com/trivedi-vatsal/python-security-audit-recipe>
- **GitHub Actions**: <https://github.com/trivedi-vatsal/python-security-audit-recipe/actions>
