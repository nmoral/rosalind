.PHONY: install test test-one cov-html lint format type check pre-commit help \
        venv-create venv-remove venv-shell venv-shell-bash venv-shell-zsh \
        venv-shell-fish venv-shell-pwsh venv-shell-cmd venv-deactivate

## help: Affiche cette aide
help:
	@grep -E '^(##|[a-zA-Z_-]+:)' Makefile | sed -e 's/^## //' -e 's/:.*##/:/g' | awk 'BEGIN {FS=":"} /^#/ {printf "\n%s\n", $$0} /^[a-zA-Z_-]+/ {printf "  %-18s %s\n", $$1, $$2}'

## install: Installe le projet en editable + deps de dev
install:
	python -m pip install -U pip setuptools wheel
	pip install -e .[dev]

## test: Lance la suite de tests (avec couverture configurée par pyproject)
test:
	python -m pytest

## test-one: Lance un test spécifique. Usage: make test-one T=path::test
test-one:
	python -m pytest $(T)

## cov-html: Génère un rapport de couverture HTML (htmlcov/index.html)
cov-html:
	python -m pytest --cov=rosalind --cov-report=term-missing --cov-report=html

## lint: Linting avec ruff
lint:
	python -m ruff check .

## format: Formatage avec ruff
format:
	python -m ruff format .

## type: Vérification de types avec mypy
type:
	python -m mypy .

## pre-commit: Installe les hooks pre-commit
pre-commit:
	pre-commit install

## check: Pack tout: lint, types, tests
check: format lint type test

## pip-upgrade: Met à jour pip/setuptools/wheel dans l'environnement actif
pip-upgrade:
	python -m pip install -U pip setuptools wheel

## sync-dev: Installe le projet en editable avec les dépendances de dev (alias de install)
sync-dev: install

## venv-shell-zsh: Ouvre un shell zsh avec la venv activée (Unix)
venv-shell-zsh:
	@zsh -lc 'test -d .venv || python -m venv .venv; source .venv/bin/activate && echo "[Makefile] venv activée. Tapez exit pour désactiver." && exec zsh -i'
