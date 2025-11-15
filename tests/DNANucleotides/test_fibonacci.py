"""Tests for the Fibonacci Rabbits problem (FIB)."""


def test_fibonacci() -> None:
    """Validate modified Fibonacci results for several inputs."""
    from rosalind.dna_nucleotides.fibonacci import fibonacci

    assert fibonacci(5, 3) == 19
    assert fibonacci(6, 3) == 40
    assert fibonacci(6, 2) == 21
    assert fibonacci(1, 2) == 1
    assert fibonacci(2, 2) == 1
