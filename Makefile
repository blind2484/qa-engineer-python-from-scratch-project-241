install:
	uv sync

gendiff:
	uv run gendiff

build:
	uv build

package-install:
	uv tool install dist/*.whl

lint:
	uv run ruff check

test:
	uv run pytest

test-coverage:
	uv run pytest --cov

test-xml:
	uv run pytest --cov --cov-report=xml