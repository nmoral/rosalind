"""Tests for counting DNA nucleotides (DNA)."""


def test_counting() -> None:
    """Return counts in the order A C G T for various inputs."""
    from rosalind.dna_nucleotides.counting import counting

    # Minimal sanity test to verify pytest runs
    assert (
        counting(
            b"AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
        )
        == "20 12 17 21"
    )
    assert counting(b"A") == "1 0 0 0"
    assert counting(b"CCGGTT") == "0 2 2 2"
