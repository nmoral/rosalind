Rosalind (src layout)

Ce projet est configuré selon le "src layout" : le code source vit dans le dossier src/ et les tests dans tests/.

Structure:
 - pyproject.toml
 - src/rosalind/
 - tests/
 - .gitignore, .editorconfig, .pre-commit-config.yaml

Prérequis:
 - Python 3.11 ou supérieur
 - pip (ou uv/poetry/hatch si vous préférez)

Installation (pip):
 1) python -m venv .venv
 2) source .venv/bin/activate   (Windows: .venv\\Scripts\\activate)
 3) pip install -e .[dev]

Commandes utiles:
 - Lancer les tests: pytest
 - Lint: ruff check .
 - Formatage: ruff format .
 - Types: mypy .

Notes:
 - tests/conftest.py ajoute automatiquement src/ au PYTHONPATH pour permettre "import rosalind" sans installation editable.
 - Le packaging utilise PEP 621 via pyproject.toml et setuptools en mode src.
