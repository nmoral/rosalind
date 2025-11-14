def test_counting() -> None:
    from rosalind.dna_nucleotides.fibonacci import fibonacci

    assert fibonacci(5, 3) == 19
    assert fibonacci(6, 3) == 40
    assert fibonacci(6, 2) == 21
    assert fibonacci(1, 2) == 1
    assert fibonacci(2, 2) == 1
