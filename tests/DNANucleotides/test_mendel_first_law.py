def test_compute_mendel_first_law() -> None:
    from rosalind.dna_nucleotides.mendel_first_law import compute_mendel_first_law

    assert compute_mendel_first_law(2, 2, 2) - 0.78333 < 0.0001
    assert compute_mendel_first_law(2, 0, 0) == 1.0
    assert compute_mendel_first_law(0, 0, 2) == 0.0
    assert compute_mendel_first_law(0, 2, 0) == 0.75
    assert compute_mendel_first_law(2, 0, 3) == 0.7
    assert compute_mendel_first_law(17, 22, 19) - 0.73960 < 0.0001


def test_probability_with_same_genotype() -> None:
    from rosalind.dna_nucleotides.mendel_first_law import probability_with_same_genotype

    assert probability_with_same_genotype(2, 6) == 1 / 15


def test_probability_with_different_genotype() -> None:
    from rosalind.dna_nucleotides.mendel_first_law import (
        probability_with_different_genotype,
    )

    assert probability_with_different_genotype(2, 2, 6) - 4 / 10 < 0.0001
