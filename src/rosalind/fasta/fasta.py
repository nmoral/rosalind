def read(raw: bytes) -> dict[str, bytes | None]:
    """Parse a single FASTA sequence.

    FASTA format starts with '>' followed by name, then the sequence
    on one or more lines.

    Args:
        raw: Raw FASTA data as bytes

    Returns:
        Dictionary with 'name' and 'value' keys

    Example:
        >>> read(b">Seq1\\nATCG\\nATCG")
        {'name': b'Seq1', 'value': b'ATCGATCG'}
    """
    fasta: dict[str, bytes | None] = {"name": None, "value": None}

    part = [line.strip() for line in raw.splitlines() if line.strip()]

    fasta["name"] = part[0].replace(b">", b"")
    fasta["value"] = b"".join(part[1::])

    return fasta


def read_multiple(raw: bytes) -> list[dict[str, bytes | None]]:
    """Parse multiple FASTA sequences from the same file.

    Args:
        raw: Raw FASTA data as bytes with multiple sequences

    Returns:
        List of dictionaries, one per sequence

    Example:
        >>> read_multiple(b">Seq1\\nATCG\\n>Seq2\\nGGGG")
        [{'name': b'Seq1', 'value': b'ATCG'}, {'name': b'Seq2', 'value': b'GGGG'}]
    """
    return [read(fasta) for fasta in raw.split(b">") if fasta.strip()]
