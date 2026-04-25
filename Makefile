.PHONY: help start build install

help:
	@echo "Model Health Documentation"
	@echo ""
	@echo "Available commands:"
	@echo "  make install   - Install dependencies"
	@echo "  make start     - Start development server"
	@echo "  make build     - Build static site"

install:
	npm install

start:
	npm start

build:
	npm run build
