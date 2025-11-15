"""Tests for reverse complement of DNA sequences (REVC)."""


def test_complementing() -> None:
    """Ensure reverse complement is computed correctly for a simple case."""
    from rosalind.dna_nucleotides.complementing import complementing

    assert complementing(b"AAAACCCGGT") == b"ACCGGGTTTT"
