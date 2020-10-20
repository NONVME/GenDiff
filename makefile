install:
	@poetry install

lint:
	@poetry run flake8 gendiff

build: lint
	@poetry build

publish: build
	@poetry publish -r testpypi

.PHONY: install lint build publish
