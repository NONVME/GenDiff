install: ## Install dependencies
	@poetry install

selfcheck: ## Checks the validity of the pyproject.toml file
	poetry check

lint: selfcheck ## Run linter
	@poetry run flake8 gendiff

test: ## Run tests
	@poetry run pytest -v

test-cov: ## Prepare coverage report for Codeclimate and tests
	@poetry run coverage run --source=gendiff -m pytest
	@poetry run coverage xml

build: lint ## Check, lint and build package
	@poetry build

publish: build ## Add package to testpypi
	@poetry publish -r testpypi

help: ## This help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: install selfcheck lint test test-cov build publish help
.DEFAULT_GOAL := help
