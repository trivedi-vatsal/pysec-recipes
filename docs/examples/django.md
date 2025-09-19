# Django Recipe 🐍

Comprehensive security automation for Django applications with multi-environment support and Django-specific security checks.

!!! success "Perfect For"

    - **Django web applications** with complex requirements
    - **Multi-environment deployments** (dev, staging, prod)
    - **Django-specific security requirements** and best practices
    - **Teams following Django conventions** and project structure

## Project Structure

```bash title="Django Project Structure"
django-app/
├── requirements/              # Environment-specific dependencies
│   ├── base.txt              # Shared dependencies
│   ├── local.txt             # Development dependencies
│   ├── production.txt        # Production dependencies
│   └── staging.txt           # Staging dependencies
├── manage.py                 # Django management script
├── myproject/               # Django project directory
│   ├── settings/
│   │   ├── base.py
│   │   ├── local.py
│   │   └── production.py
│   └── urls.py
└── .github/workflows/
    └── django-security.yml  # Django security workflow
```

## Requirements Structure

=== "base.txt"

    ```text title="requirements/base.txt"
    # Core Django dependencies
    Django>=4.2.0,<5.0
    psycopg2-binary>=2.9.0
    celery>=5.3.0
    redis>=4.5.0
    django-environ>=0.10.0
    Pillow>=10.0.0
    ```

=== "production.txt"

    ```text title="requirements/production.txt"
    -r base.txt

    # Production-specific dependencies
    gunicorn>=21.0.0
    whitenoise>=6.5.0
    sentry-sdk>=1.28.0
    django-redis>=5.3.0
    boto3>=1.28.0
    ```

=== "local.txt"

    ```text title="requirements/local.txt"
    -r base.txt

    # Development dependencies
    django-debug-toolbar>=4.2.0
    django-extensions>=3.2.0
    pytest-django>=4.5.0
    black>=23.0.0
    flake8>=6.0.0
    ```

=== "staging.txt"

    ```text title="requirements/staging.txt"
    -r production.txt

    # Staging-specific dependencies
    django-debug-toolbar>=4.2.0  # For debugging in staging
    ```

## Complete Django Security Workflow

???+ example "Complete django-security.yml"

    This workflow provides comprehensive security scanning for all Django environments plus Django-specific security checks.

    ```yaml title=".github/workflows/django-security.yml" linenums="1"
    name: Django Security Audit

    on:
      schedule:
        - cron: "0 9 * * 1"  # Monday 9 AM UTC
      workflow_dispatch:
      push:
        branches: [main, develop]
        paths: 
          - "requirements/*.txt"
          - ".github/workflows/django-security.yml"

    env:
      PYTHON_VERSION: "3.11"

    jobs:
      django-security:
        name: Django Security Audit
        runs-on: ubuntu-latest
        permissions:
          contents: read
          issues: write
          security-events: write
        
        strategy:
          matrix:
            environment: [local, staging, production]
            
        steps:
          - name: Checkout repository
            uses: actions/checkout@v4

          - name: Set up Python
            uses: actions/setup-python@v4
            with:
              python-version: ${{ env.PYTHON_VERSION }}

          - name: Install uv
            uses: astral-sh/setup-uv@v3

          - name: Install pip-audit
            run: uv pip install --system pip-audit

          - name: Install Django dependencies
            run: |
              uv pip install --system -r requirements/${{ matrix.environment }}.txt

          - name: Run pip-audit on ${{ matrix.environment }}
            run: |
              mkdir -p audit-outputs
              pip-audit -r requirements/${{ matrix.environment }}.txt \
                --format json \
                --output audit-outputs/audit-${{ matrix.environment }}.json

          - name: Run Django security checks
            env:
              DJANGO_SETTINGS_MODULE: myproject.settings.production
            run: |
              python manage.py check --deploy --settings=myproject.settings.production

          - name: Upload audit results
            uses: actions/upload-artifact@v4
            with:
              name: django-security-audit-${{ matrix.environment }}
              path: audit-outputs/
    ```

## Django-Specific Security Features

This recipe includes specialized Django security features:

!!! tip "Django Security Enhancements"

    === "🛡️ Django Security Checks"

        ```bash title="Integrated Django security validation"
        # Runs Django's built-in security checks
        python manage.py check --deploy
        
        # Validates production settings for:
        # - DEBUG = False
        # - SECRET_KEY security
        # - ALLOWED_HOSTS configuration
        # - SSL/HTTPS settings
        # - Session security
        # - CSRF protection
        ```

    === "📦 Multi-Environment Scanning"

        - **Local environment** - Development dependencies
        - **Staging environment** - Near-production setup
        - **Production environment** - Production-only packages
        - **Matrix strategy** - Parallel scanning of all environments

    === "🎯 Django-Optimized Dependencies"

        Common Django packages are automatically scanned:
        - Django framework and extensions
        - Database drivers (PostgreSQL, MySQL)
        - Web servers (Gunicorn, uWSGI)
        - Caching (Redis, Memcached)
        - Storage (AWS S3, Google Cloud)

## Quick Setup Instructions

=== "One-Command Setup"

    !!! tip "Fastest Django Setup"

        ```bash title="Django-specific installation"
        curl -sSL https://raw.githubusercontent.com/trivedi-vatsal/python-security-audit-recipe/main/django-setup.py | python3
        ```

=== "Manual Setup"

    !!! example "Step-by-step Django installation"

        1. **Create workflow directory:**

            ```bash
            mkdir -p .github/workflows
            ```

        2. **Download Django workflow:**

            ```bash
            curl -o .github/workflows/django-security.yml \
              https://raw.githubusercontent.com/trivedi-vatsal/python-security-audit-recipe/main/.github/workflows/django-security.yml
            ```

        3. **Set up requirements structure** (if not already done):

            ```bash
            mkdir -p requirements
            # Create your base.txt, production.txt, etc.
            ```

        4. **Update Django settings module** in the workflow file to match your project

## Django-Specific Verification

!!! check "Test Your Django Setup"

    1. **Verify workflow runs** for all environments
    2. **Check Django security checks** pass
    3. **Confirm issue creation** works for vulnerabilities
    4. **Test manual triggers** work correctly

    **Django-Specific Validations:**
    - ✅ All environment requirements scan successfully
    - ✅ Django security checks pass
    - ✅ Matrix strategy runs parallel scans
    - ✅ Django-specific vulnerabilities detected

## What This Recipe Provides

Your Django application will have:

- **🔄 Multi-environment security scanning** - Local, staging, production
- **🛡️ Django security validation** - Built-in security checks
- **📱 Automatic issue creation** - When vulnerabilities are found
- **🔍 Comprehensive coverage** - All Django-specific dependencies
- **⚡ Parallel scanning** - Fast execution with matrix strategy

## Ready for More Advanced Setups?

Once your Django recipe is working well:

- **[FastAPI Recipe](fastapi.md)** - For API-only services
- **[Enterprise Recipe](multi-environment.md)** - For complex deployments  
- **[Monorepo Recipe](monorepo.md)** - For multiple Django apps
