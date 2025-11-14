def test_counting() -> None:
    from rosalind.dna_nucleotides.counting import counting

    # Test de santé minimal pour vérifier que pytest s'exécute
    assert (
        counting(b"AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC")
        == "20 12 17 21"
    )
    assert counting(b"A") == "1 0 0 0"
    assert counting(b"CCGGTT") == "0 2 2 2"
