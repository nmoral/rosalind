def counting(dna: bytes) -> str:
    """Count occurrences of each nucleotide in a DNA sequence.

    Args:
        dna: DNA sequence as bytes (e.g., b"ATCG")

    Returns:
        Space-separated counts as string: "A C G T"

    Example:
        >>> counting(b"AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC")
        '20 12 17 21'
    """

    count = do_counting(dna)

    return (
        f"{count.get(ord('A'), 0)} "
        f"{count.get(ord('C'), 0)} "
        f"{count.get(ord('G'), 0)} "
        f"{count.get(ord('T'), 0)}"
    )


def do_counting(dna: bytes) -> dict[int, int]:
    """Count occurrences of each byte in a sequence.

    Helper function used by counting() and gc_content().

    Args:
        dna: Sequence as bytes

    Returns:
        Dictionary mapping byte values to their counts
    """
    count: dict[int, int] = {}

    for n in dna:
        count[n] = count.get(n, 0) + 1
    return count
