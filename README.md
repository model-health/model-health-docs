# Model Health Documentation

Product documentation for Model Health, built with [Docusaurus](https://docusaurus.io/). Hosted at [docs.modelhealth.io](https://docs.modelhealth.io).

For SDK documentation, see [model-health-sdk-docs](https://github.com/model-health/model-health-sdk-docs) → [sdk.modelhealth.io](https://sdk.modelhealth.io).

## Local Development

### Prerequisites

- Node.js 20+

### Setup
```bash
make install
```

### Development server
```bash
make dev
```

Starts a local development server at `http://localhost:3000`. Note: search is unavailable in dev mode.

### Production preview (with search)
```bash
make prod
```

Builds the site and serves it locally at `http://localhost:3000`.

## Project Structure
```
model-health-docs/
├── .github/
│   └── workflows/
│       └── deploy.yml          # GitHub Actions deployment
├── docs/                       # Documentation markdown files
├── src/
│   ├── css/                    # Custom CSS
│   ├── pages/                  # Custom pages
│   └── theme/                  # Swizzled Docusaurus components
├── static/                     # Static assets
│   └── img/
├── docusaurus.config.js        # Docusaurus configuration
├── docs-sidebars.js            # Sidebar navigation
└── package.json
```

## Releasing

To cut a new release:

```bash
make release
```

The script will:
1. Show the current version (from the latest git tag)
2. Ask whether to bump major, minor or patch
3. Update `package.json`
4. Commit, tag and push (no push if `--dry-run` is specified as a command line argument)

CI generates `version.json` from the tag at build time — this file is not committed.

This script will only run on `main`, to override this use `--force`.
