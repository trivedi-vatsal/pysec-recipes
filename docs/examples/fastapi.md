# FastAPI Recipe ⚡

Modern security automation for FastAPI applications with production/development separation and async-focused optimizations.

!!! success "Perfect For"

    - **FastAPI REST APIs** and web services
    - **Modern async Python applications** using async/await
    - **Microservices architecture** and cloud-native apps
    - **API-first development** with OpenAPI integration

## Project Structure

```bash title="FastAPI Project Structure"
fastapi-app/
├── requirements.txt          # Production dependencies
├── requirements-dev.txt      # Development dependencies
├── main.py                   # FastAPI application
├── app/                      # Application modules
│   ├── __init__.py
│   ├── models.py
│   ├── routers/
│   └── database.py
└── .github/workflows/
    └── fastapi-security.yml  # FastAPI security workflow
```

## FastAPI Requirements Structure

=== "requirements.txt"

    ```text title="requirements.txt"
    # Core FastAPI stack
    fastapi>=0.103.0
    uvicorn[standard]>=0.23.0
    pydantic>=2.3.0
    pydantic-settings>=2.0.0

    # Database and ORM
    sqlalchemy>=2.0.0
    alembic>=1.11.0
    asyncpg>=0.28.0  # or aiomysql

    # Production dependencies
    python-multipart>=0.0.6
    python-jose[cryptography]>=3.3.0
    passlib[bcrypt]>=1.7.4
    ```

=== "requirements-dev.txt"

    ```text title="requirements-dev.txt"
    -r requirements.txt

    # Testing framework
    pytest>=7.4.0
    pytest-asyncio>=0.21.0
    httpx>=0.24.0
    pytest-cov>=4.1.0

    # Development tools
    black>=23.0.0
    flake8>=6.0.0
    mypy>=1.5.0
    pre-commit>=3.3.0

    # Documentation
    mkdocs-material>=9.2.0
    ```

## Complete FastAPI Security Workflow

???+ example "Complete fastapi-security.yml"

    This workflow provides optimized security scanning for FastAPI applications with separate prod/dev analysis.

    ```yaml title=".github/workflows/fastapi-security.yml" linenums="1"
    name: FastAPI Security Audit

    on:
      schedule:
        - cron: "0 10 * * 1"  # Monday 10 AM UTC
      workflow_dispatch:
      push:
        branches: [main, develop]
        paths: 
          - "requirements*.txt"
          - ".github/workflows/fastapi-security.yml"

    env:
      PYTHON_VERSION: "3.11"

    jobs:
      fastapi-security:
        name: FastAPI Security Audit
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

          - name: Install pip-audit
            run: uv pip install --system pip-audit

          - name: Create outputs directory
            run: mkdir -p audit-outputs

          - name: Audit production dependencies
            run: |
              echo "🔍 Scanning production dependencies..."
              pip-audit -r requirements.txt \
                --format json \
                --output audit-outputs/audit-production.json \
                --desc

          - name: Audit development dependencies
            run: |
              echo "🔍 Scanning development dependencies..."
              pip-audit -r requirements-dev.txt \
                --format json \
                --output audit-outputs/audit-development.json \
                --desc || true

          - name: Process FastAPI results
            run: |
              echo "📊 Processing audit results..."
              
              # Count production vulnerabilities
              PROD_VULNS=$(jq '[.dependencies[].vulns[]] | length' audit-outputs/audit-production.json 2>/dev/null || echo "0")
              echo "PROD_VULNS=$PROD_VULNS" >> $GITHUB_ENV
              
              # Count development vulnerabilities
              if [ -f audit-outputs/audit-development.json ]; then
                DEV_VULNS=$(jq '[.dependencies[].vulns[]] | length' audit-outputs/audit-development.json 2>/dev/null || echo "0")
              else
                DEV_VULNS=0
              fi
              echo "DEV_VULNS=$DEV_VULNS" >> $GITHUB_ENV
              
              echo "Production vulnerabilities: $PROD_VULNS"
              echo "Development vulnerabilities: $DEV_VULNS"

          - name: Upload FastAPI audit results
            uses: actions/upload-artifact@v4
            with:
              name: fastapi-security-audit-results
              path: audit-outputs/
              retention-days: 90

          - name: Fail on production vulnerabilities
            if: env.PROD_VULNS != '0'
            run: |
              echo "❌ Found ${{ env.PROD_VULNS }} vulnerabilities in production dependencies!"
              echo "Check the uploaded artifacts for detailed vulnerability information."
              exit 1
    ```

## FastAPI-Specific Security Features

This recipe includes FastAPI-optimized security features:

!!! tip "FastAPI Security Enhancements"

    === "🚀 Production Focus"

        ```bash title="Production-critical scanning"
        # Strict scanning for production dependencies
        pip-audit -r requirements.txt --format json --desc
        
        # Fails CI/CD if production vulnerabilities found
        # Development vulnerabilities logged but don't fail build
        ```

    === "🔄 Async-Optimized Dependencies"

        FastAPI-specific packages automatically scanned:
        - **FastAPI framework** and extensions
        - **Async HTTP clients** (httpx, aiohttp)
        - **Async database drivers** (asyncpg, aiomysql)
        - **ASGI servers** (uvicorn, hypercorn)
        - **Async task queues** (celery, arq)

    === "📱 API Security Focus"

        Special attention to API security dependencies:
        - **Authentication** (python-jose, passlib)
        - **Validation** (pydantic, email-validator)
        - **CORS and middleware** security
        - **OpenAPI** documentation security

## Quick Setup Instructions

=== "One-Command Setup"

    !!! tip "Fastest FastAPI Setup"

        ```bash title="FastAPI-specific installation"
        curl -sSL https://raw.githubusercontent.com/trivedi-vatsal/python-security-audit-recipe/main/fastapi-setup.py | python3
        ```

=== "Manual Setup"

    !!! example "Step-by-step FastAPI installation"

        1. **Create workflow directory:**

            ```bash
            mkdir -p .github/workflows
            ```

        2. **Download FastAPI workflow:**

            ```bash
            curl -o .github/workflows/fastapi-security.yml \
              https://raw.githubusercontent.com/trivedi-vatsal/python-security-audit-recipe/main/.github/workflows/fastapi-security.yml
            ```

        3. **Ensure requirements structure:**

            ```bash
            # Make sure you have both files:
            # requirements.txt (production)
            # requirements-dev.txt (development)
            ```

## FastAPI-Specific Verification

!!! check "Test Your FastAPI Setup"

    1. **Verify both production and development** scans work
    2. **Check production vulnerabilities fail** the workflow
    3. **Confirm development vulnerabilities** are logged but don't fail
    4. **Test manual triggers** work correctly

    **FastAPI-Specific Validations:**
    - ✅ Production dependencies scan successfully
    - ✅ Development dependencies scan (with tolerance)
    - ✅ FastAPI-specific packages detected
    - ✅ API security dependencies validated

## What This Recipe Provides

Your FastAPI application will have:

- **🚀 Production-focused security** - Critical for API services
- **⚡ Fast parallel scanning** - Optimized for CI/CD
- **📱 API-specific validation** - FastAPI and async packages
- **🔍 Comprehensive coverage** - Production and development deps
- **🛡️ Smart failure logic** - Fail on prod, warn on dev vulnerabilities

## Ready for More Complex Setups?

Once your FastAPI recipe is working:

- **[Enterprise Recipe](multi-environment.md)** - For multiple environments
- **[Monorepo Recipe](monorepo.md)** - For multiple FastAPI services  
- **[Django Recipe](django.md)** - If you also have Django services
