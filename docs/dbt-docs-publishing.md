# dbt Docs Publishing (GitHub Pages)

This project publishes dbt documentation for `modules/revenue-intelligence/dbt` using:
- `.github/workflows/dbt-docs.yml`

## 1. Enable GitHub Pages

In repository settings:
1. Open `Settings -> Pages`
2. In `Build and deployment`, set `Source` to `GitHub Actions`

## 2. Repository secrets

No secrets are required for docs publishing.
The workflow uses a local `duckdb` target in CI and generates docs with
`--empty-catalog` to publish lineage/documentation reliably.

## 3. Run the workflow

Option A:
- Trigger `dbt-docs` manually from `Actions -> dbt-docs -> Run workflow`

Option B:
- Push to `main` changing files under `modules/revenue-intelligence/dbt/**`

## 4. Verify publication

After a successful run, open:
- `https://<github-user>.github.io/revenue-intelligence-platform-suite/`

If publication fails, check:
- Pages source configuration
- repository Actions permissions
