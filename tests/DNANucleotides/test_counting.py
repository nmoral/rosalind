def test_pytest_running() -> None:
    from rosalind.dna_nucleotides.counting import counting

    # Test de santé minimal pour vérifier que pytest s'exécute
    assert (
        counting("AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC")
        == "20 12 17 21"
    )
    assert counting("A") == "1 0 0 0"
    assert counting("CCGGTT") == "0 2 2 2"
