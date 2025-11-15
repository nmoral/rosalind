def counting_mutations(s: bytes, t: bytes) -> int:
    """Calculate the Hamming distance between two sequences.

    The Hamming distance is the number of positions at which the
    corresponding symbols differ. Sequences must have equal length.

    Args:
        s: First DNA sequence as bytes
        t: Second DNA sequence as bytes (same length as s)

    Returns:
        Number of differing positions (Hamming distance)

    Example:
        >>> counting_mutations(b"GAGCCTACTAACGGGAT", b"CATCGTAATGACGGCCT")
        7

    Note:
        Time complexity: O(n) where n = sequence length
    """
    count = 0
    for i in range(len(s)):
        count = count + 1 if s[i] != t[i] else count

    return count
