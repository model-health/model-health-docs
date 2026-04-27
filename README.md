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

## Deployment

Documentation is automatically deployed to GitHub Pages at `https://docs.modelhealth.io` on every push to `main`.

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

## Updating Documentation

All content in `docs/`, `src/` and `static/img/` can be modified and committed directly. Changes deploy automatically on push to `main`.

## Custom Domain

The custom domain `docs.modelhealth.io` is configured via:
- `static/CNAME` file
- AWS Route 53: `docs.modelhealth.io` → CNAME → `model-health.github.io`
- GitHub Pages custom domain settings
