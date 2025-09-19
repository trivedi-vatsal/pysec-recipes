# Monorepo Example

Complex setup for monorepos with multiple Python services, featuring dynamic service discovery.

## Project Structure

```bash title="Monorepo Directory Structure"
monorepo/
├── services/
│   ├── api/
│   │   └── requirements.txt
│   ├── worker/
│   │   └── requirements.txt
│   └── scheduler/
│       └── requirements.txt
└── .github/workflows/
    └── monorepo-security.yml
```

## Workflow File

```yaml title=".github/workflows/monorepo-security.yml" linenums="1"
name: Monorepo Security Audit

on:
  schedule:
    - cron: "0 8 * * 1"
  workflow_dispatch:

jobs:
  find-services:
    runs-on: ubuntu-latest
    outputs:
      services: ${{ steps.find.outputs.services }}
    steps:
      - uses: actions/checkout@v4
      - id: find
        run: |
          services=$(find services -name "requirements.txt" -exec dirname {} \; | sort | jq -R . | jq -s .)
          echo "services=$services" >> $GITHUB_OUTPUT

  security-audit:
    needs: find-services
    runs-on: ubuntu-latest
    strategy:
      matrix:
        service: ${{ fromJson(needs.find-services.outputs.services) }}
    
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Install pip-audit
        run: pip install pip-audit
      
      - name: Audit ${{ matrix.service }}
        run: |
          cd "${{ matrix.service }}"
          pip-audit -r requirements.txt \
            --format json \
            --output "../audit-$(basename ${{ matrix.service }}).json"
      
      - name: Upload results
        uses: actions/upload-artifact@v4
        with:
          name: audit-$(basename ${{ matrix.service }})
          path: audit-*.json
```

## Advanced Features

- **Dynamic service discovery** using `find` command
- **Two-job workflow** with dependency between jobs
- **Matrix strategy** for parallel execution per service
- **Separate artifacts** for each service
- **Flexible service structure** - automatically detects new services

## Use Case

Perfect for:

- Large monorepos with multiple Python services
- Microservices architecture in a single repository
- Organizations with many small Python applications
- Projects where services are added/removed frequently
