def test_import_and_version() -> None:
    import rosalind

    assert hasattr(rosalind, "__version__")


def test_pytest_running() -> None:
    from rosalind.example import add

    # Test de santé minimal pour vérifier que pytest s'exécute
    assert add(1, 1) == 2
