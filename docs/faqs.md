# Frequently Asked Questions (FAQs)

Common questions and answers about the Python Security Audit Recipe.

## Getting Started

???+ question "What is the Python Security Audit Recipe?"

    The Python Security Audit Recipe is a GitHub Actions workflow that automatically scans your Python dependencies for security vulnerabilities using `pip-audit`. It creates GitHub issues when vulnerabilities are found and provides detailed remediation guidance.

???+ question "Do I need any special knowledge to use this?"

    No! The recipe is designed to work out-of-the-box with zero configuration. If you have a Python project with a `requirements.txt` file, you can set it up in 30 seconds.

???+ question "Is this free to use?"

    Yes! The recipe is completely free and open-source (MIT license). It runs on GitHub Actions, which provides free compute minutes for public repositories.

## Installation & Setup

???+ question "What files do I need in my repository?"

    You need:

    - A `requirements.txt` file (or similar dependency file)
    - The workflow file in `.github/workflows/security-audit.yml`
    - Optional: Issue templates in `.github/ISSUE_TEMPLATE/`

???+ question "Can I use this with private repositories?"

    Yes! The recipe works with both public and private repositories. Private repositories get 2,000 free GitHub Actions minutes per month.

???+ question "What if I don't have a `requirements.txt` file?"

    You'll need a dependency file that `pip-audit` can read:

    - `requirements.txt` (most common)
    - `pyproject.toml` 
    - `setup.py`
    - Or install dependencies directly in the workflow

???+ question "How do I enable GitHub Actions in my repository?"

    GitHub Actions are enabled by default. Just add the workflow file to `.github/workflows/` and it will run automatically.

## Workflow & Scanning

???+ question "How often does the security scan run?"

    By default:

    - **Weekly** on Mondays at 8 AM UTC (scheduled)
    - **On push** when `requirements.txt` changes
    - **Manual trigger** from the GitHub Actions tab

???+ question "Can I change the scan schedule?"

    Yes! Edit the `cron` expression in the workflow file:

    ```yaml
    schedule:
      - cron: "0 8 * * 1"  # Weekly on Monday
      # - cron: "0 2 * * *"  # Daily at 2 AM
      # - cron: "0 8 * * 1,4"  # Monday and Thursday
    ```

???+ question "What vulnerability databases does it use?"

    The recipe uses `pip-audit`, which checks multiple databases:

    - **PyPI Advisory Database**
    - **OSV (Open Source Vulnerabilities)**
    - **Python Packaging Advisory Database**

???+ question "Does the scan slow down my CI/CD pipeline?"

    The scan typically takes 1-3 minutes. You can configure it to run only on schedule (not on every push) to avoid slowing down development.

## Issues & Notifications

???+ question "Will it create a new issue for every scan?"

    No! The recipe is smart:

    - **Creates** one issue when vulnerabilities are first found
    - **Updates** the same issue with new scan results
    - **Closes** the issue when vulnerabilities are resolved
    - **Creates clean reports** weekly when no vulnerabilities exist

???+ question "How do I know when vulnerabilities are found?"

    You'll get notified through:

    - **GitHub issue creation** (with email notification if enabled)
    - **GitHub Actions failure** (if configured to fail on vulnerabilities)
    - **Issue comments** when vulnerabilities are resolved

???+ question "Can I customize the issue templates?"

    Yes! The issue templates are in `.github/ISSUE_TEMPLATE/`. You can modify:

    - Issue titles and labels
    - Content structure and formatting
    - Additional information sections

## Vulnerability Management

???+ question "What should I do when vulnerabilities are found?"

    Follow this process:

    1. **Review** the created GitHub issue for details
    2. **Update** affected packages to recommended versions
    3. **Test** your application after updates
    4. **Re-run** the workflow to verify fixes

???+ question "Can I ignore specific vulnerabilities?"

    Yes! Add exclusions to the workflow:

    ```yaml
    pip-audit -r requirements.txt \
      --ignore-vuln CVE-2023-12345 \
      --ignore-vuln GHSA-xxxx-xxxx-xxxx
    ```

???+ question "What if a vulnerability has no fix available?"

    Document the risk assessment:

    1. **Evaluate** if the vulnerability affects your use case
    2. **Consider** alternative packages
    3. **Add to ignore list** if risk is acceptable
    4. **Monitor** for future fixes

## Advanced Configuration

???+ question "Can I scan multiple requirements files?"

    Yes! Check out our examples:

    - **[Multi-Environment Recipe](examples/multi-environment.md)** - For dev/staging/prod
    - **[Django Recipe](examples/django.md)** - For Django projects
    - **[Monorepo Recipe](examples/monorepo.md)** - For multiple services

???+ question "How do I customize Python version?"

    Update the `PYTHON_VERSION` environment variable:

    ```yaml
    env:
      PYTHON_VERSION: "3.11"  # Change to your version
    ```

???+ question "Can I integrate with Slack or Teams?"

    Yes! Add notification steps to the workflow:

    ```yaml
    - name: Notify Slack
      if: env.AUDIT_STATUS == 'vulnerabilities_found'
      uses: rtCamp/action-slack-notify@v2
      env:
        SLACK_WEBHOOK: ${{ secrets.SLACK_WEBHOOK }}
    ```

???+ question "Does it work with Poetry or Pipenv?"

    Currently optimized for `requirements.txt`. For other tools:

    - **Poetry**: Export requirements: `poetry export -f requirements.txt > requirements.txt`
    - **Pipenv**: Export requirements: `pipenv requirements > requirements.txt`
    - **Future**: Direct support planned for upcoming releases

## Troubleshooting

???+ question "The workflow is failing with 'pip-audit not found'"

    Ensure the workflow installs pip-audit:

    ```yaml
    - name: Install pip-audit
      run: uv pip install --system pip-audit
    ```

???+ question "No issues are being created despite vulnerabilities"

    Check repository permissions:

    1. Go to **Settings** → **Actions** → **General**
    2. Set **Workflow permissions** to "Read and write permissions"
    3. Enable "Allow GitHub Actions to create and approve pull requests"

???+ question "The workflow runs but finds no dependencies"

    Verify your requirements file:

    - Check file exists: `requirements.txt`
    - Check file has content (not empty)
    - Check file path in workflow matches your structure

???+ question "Can I run this locally before pushing?"

    Yes! Install pip-audit locally:

    ```bash
    pip install pip-audit
    pip-audit -r requirements.txt
    ```

## Performance & Limits

???+ question "Are there any GitHub Actions limits I should know about?"

    GitHub provides:

    - **Public repos**: Unlimited minutes
    - **Private repos**: 2,000 free minutes/month
    - **Workflow runs**: Max 6 hours per run
    - **Artifacts**: 90-day retention (configurable)

???+ question "How much storage do the artifacts use?"

    Audit artifacts are typically small:

    - **JSON results**: 1-10 KB
    - **Markdown reports**: 2-20 KB
    - **Total per run**: Usually under 100 KB

???+ question "Can I reduce the scan frequency to save minutes?"

    Yes! For private repos, consider:

    - **Monthly scans**: `cron: "0 8 1 * *"`
    - **Manual only**: Remove `schedule` section
    - **Critical changes only**: Scan only on requirements.txt changes

## Integration & Compatibility

???+ question "Does this work with GitHub Enterprise?"

    Yes! The recipe works with:

    - GitHub.com (public/private repos)
    - GitHub Enterprise Server
    - GitHub Enterprise Cloud

???+ question "Can I use this with other security tools?"

    Absolutely! Combine with:

    - **Bandit** for static code analysis
    - **Safety** for additional vulnerability checking
    - **Snyk** for comprehensive security scanning
    - **CodeQL** for semantic code analysis

???+ question "Is this compatible with dependabot?"

    Yes! They complement each other:

    - **Dependabot**: Creates PRs for dependency updates
    - **Security Recipe**: Monitors for vulnerabilities and creates issues
    - Use both for comprehensive dependency management

## Getting Help

???+ question "Where can I get support?"

    Several options:

    - **GitHub Issues**: Report bugs or request features
    - **Documentation**: Comprehensive guides in the `/docs` folder
    - **Examples**: Real-world implementations in `/examples`
    - **Community**: GitHub Discussions (if enabled)

???+ question "How do I contribute to the project?"

    Contributions welcome!

    1. **Fork** the repository
    2. **Create** a feature branch
    3. **Submit** a pull request
    4. **Follow** the contribution guidelines

???+ question "Can I suggest new features?"

    Yes! Open a GitHub issue with:

    - **Feature description**
    - **Use case explanation**
    - **Implementation ideas** (if any)

---

!!! info "Still have questions?"

    Open an issue on [GitHub](https://github.com/trivedi-vatsal/python-security-audit-recipe/issues) or check our [documentation](index.md) for more details!
 
 