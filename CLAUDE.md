# CLAUDE.md

Repo-specific guidance for `model-health-docs`. Shared platform context is auto-loaded
from the parent folder; generic coding behavior from `~/.claude/CLAUDE.md`.

## Where this repo sits

Documentation for the platform to help users understand and configure the Model Health 
system.

## Stack

Docusaurus 3 (React 19), with `@easyops-cn/docusaurus-search-local` for local search.
Docs live in `docs/` as MDX/MD, sidebar structure is in `docs-sidebars.js`.

## Build / preview

- `make install` - install dependencies
- `make dev` - start dev server at `http://localhost:3000` (search unavailable)
- `make build` - build static site
- `make prod` - build and serve production build at `http://localhost:3000` (search works)
- `make clean` - remove `build/` and `.docusaurus/` cache

Tagging `main` with a new version will automaticaly kick off a deployment.

## Gotchas

- Sentence case, concise.
- Filenames should always be `lower-case-kebab.ext` - any imported files that don't 
  match this should be renamed.
- MDX and MD files that contain an ID should reuse the filename as the ID
