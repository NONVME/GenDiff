install:
	@poetry install

lint:
	@poetry run flake8 gendiff

test:
	@poetry run pytest -v

test-cov:
	@poetry run pytest --cov=gendiff tests --cov-report xml

build: lint
	@poetry build

publish: build
	@poetry publish -r testpypi

.PHONY: install lint build publish
