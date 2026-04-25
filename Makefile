.PHONY: help start build install clean

help:
	@echo "Model Health Documentation"
	@echo ""
	@echo "Available commands:"
	@echo "  make install   - Install dependencies"
	@echo "  make start     - Start development server"
	@echo "  make build     - Build static site"
	@echo "  make clean     - Remove build/ and .docusaurus/ cache"

install:
	npm install

start:
	npm start

build:
	npm run build

clean:
	rm -rf build .docusaurus
