# Multi-Environment Example

For projects with separate requirements files for different environments.

## Project Structure

```bash title="Multi-Environment Project Structure"
my-app/
├── requirements/
│   ├── base.txt
│   ├── development.txt
│   ├── production.txt
│   └── testing.txt
└── .github/workflows/
    └── multi-env-security.yml
```

## Workflow File

```yaml title=".github/workflows/multi-env-security.yml" linenums="1"
name: Multi-Environment Security Audit

on:
  schedule:
    - cron: "0 8 * * 1"
  workflow_dispatch:
  push:
    branches: [main]
    paths: ["requirements/*.txt"]

jobs:
  security-audit:
    name: Security Audit (${{ matrix.environment }})
    runs-on: ubuntu-latest
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
          python-version: '3.11'

      - name: Install pip-audit
        run: pip install pip-audit

      - name: Run security audit for ${{ matrix.environment }}
        run: |
          mkdir -p audit-outputs

          if [ -f "${{ matrix.requirements }}" ]; then
            pip-audit -r "${{ matrix.requirements }}" \
              --format json \
              --output "audit-outputs/audit-${{ matrix.environment }}.json" || true
            
            pip-audit -r "${{ matrix.requirements }}" \
              --format markdown \
              --output "audit-outputs/audit-${{ matrix.environment }}.md" || true
          else
            echo "Requirements file not found: ${{ matrix.requirements }}"
            echo '{"dependencies": []}' > "audit-outputs/audit-${{ matrix.environment }}.json"
          fi

      - name: Process results for ${{ matrix.environment }}
        run: |
          if [ -f "audit-outputs/audit-${{ matrix.environment }}.json" ]; then
            VULN_COUNT=$(jq '[.dependencies[].vulns[]] | length' "audit-outputs/audit-${{ matrix.environment }}.json")
            echo "Environment: ${{ matrix.environment }} - Vulnerabilities: $VULN_COUNT"
          fi

      - name: Upload audit artifacts
        uses: actions/upload-artifact@v4
        with:
          name: security-audit-${{ matrix.environment }}-${{ github.run_number }}
          path: audit-outputs/
          retention-days: 30
```

## Features

- **Parallel scanning** of multiple environments
- **Matrix strategy** for efficient execution
- **Separate artifacts** for each environment
- **Handles missing files** gracefully

## Use Case

Perfect for:

- Projects with development/staging/production environments
- Applications with different dependency sets per environment
- Teams that need environment-specific security reports
