import os
import sys


def _ensure_src_on_path() -> None:
    """Ajoute le dossier 'src' au sys.path pour permettre `import rosalind` en dev.

    Évite d'avoir à installer le package en mode editable pendant le développement.
    """

    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    src_path = os.path.join(repo_root, "src")
    if src_path not in sys.path:
        sys.path.insert(0, src_path)


_ensure_src_on_path()
