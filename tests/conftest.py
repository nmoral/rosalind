import os
import sys


def _ensure_src_on_path() -> None:
    """Add 'src' folder to sys.path to allow `import rosalind` in dev mode.

    Avoids having to install the package in editable mode during development.
    """

    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    src_path = os.path.join(repo_root, "src")
    if src_path not in sys.path:
        sys.path.insert(0, src_path)


_ensure_src_on_path()
