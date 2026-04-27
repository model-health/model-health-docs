.PHONY: help start build serve install clean release

help:
	@echo "Model Health Documentation"
	@echo ""
	@echo "Available commands:"
	@echo "  make install   - Install dependencies"
	@echo "  make dev       - Start development server (search unavailable)"
	@echo "  make build     - Build static site"
	@echo "  make prod      - Serve the production build (search works here)"
	@echo "  make clean     - Remove build/ and .docusaurus/ cache"
	@echo "  make release   - Bump version, tag and push a new release"

install:
	npm install

dev:
	npm start

build:
	npm run build

prod: build
	npm run serve

clean:
	rm -rf build .docusaurus

release:
	python3 scripts/release.py
