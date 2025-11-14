def test_counting() -> None:
    from rosalind.dna_nucleotides.complementing import complementing

    assert complementing(b"AAAACCCGGT") == b"ACCGGGTTTT"
