def complementing(dna: bytes) -> bytes:
    """Return the reverse complement of a DNA sequence.

    The reverse complement is obtained by:
    1. Replacing each base with its complement (A<->T, C<->G)
    2. Reversing the sequence order (5' to 3' direction)

    Args:
        dna: DNA sequence as bytes (e.g., b"ATCG")

    Returns:
        Reverse complement as bytes (e.g., b"CGAT")

    Example:
        >>> complementing(b"AAAACCCGGT")
        b'ACCGGGTTTT'
    """
    return dna.translate(bytes.maketrans(b"ATCG", b"TAGC"))[::-1]
