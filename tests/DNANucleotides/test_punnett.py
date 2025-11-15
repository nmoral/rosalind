def test_punnett() -> None:
    from rosalind.dna_nucleotides.punnett import generate_punnett

    assert generate_punnett("AA", "aa") == ["Aa", "Aa", "Aa", "Aa"]
    assert generate_punnett("Aa", "aA") == ["Aa", "aa", "AA", "aA"]


def test_compute_punnett_probability() -> None:
    from rosalind.dna_nucleotides.punnett import (
        compute_punnett_probability,
        generate_punnett,
    )

    punnett_square = generate_punnett("Aa", "aA")

    assert compute_punnett_probability(punnett_square, "A") == 3 / 4

    punnett_square = generate_punnett("AA", "aa")
    assert compute_punnett_probability(punnett_square, "A") == 4 / 4

    punnett_square = generate_punnett("aa", "aa")
    assert compute_punnett_probability(punnett_square, "A") == 0 / 4
