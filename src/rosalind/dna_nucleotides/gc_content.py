from rosalind.dna_nucleotides.counting import do_counting
from rosalind.fasta.fasta import read_multiple


def gc_content(dna_fasta: bytes) -> str:
    """Find the sequence with highest GC content from FASTA input.

    Args:
        dna_fasta: Multiple DNA sequences in FASTA format

    Returns:
        Formatted string with sequence name and GC percentage

    Example:
        >>> gc_content(b">Seq1\\nATCG\\n>Seq2\\nGGCC")
        "Seq2\\n100.000000\\n"
    """
    fasta = find_max_gc_content(dna_fasta)
    name: bytes | float | None = fasta.get("name", b"")
    name_str: str = ""
    percent: bytes | float | None = fasta.get("percent", 0.0)
    percent_float: float = 0.0
    if isinstance(name, bytes):
        name_str = name.decode("utf-8")
    if isinstance(percent, float):
        percent_float = percent

    return f"{name_str}\n{percent_float:.6f}\n"


def find_max_gc_content(raw: bytes) -> dict[str, bytes | float | None]:
    """Find the sequence with maximum GC content.

    Args:
        raw: FASTA format data as bytes

    Returns:
        Dictionary with 'name' and 'percent' keys for max GC sequence
    """
    b: float = 0.0
    max_fasta: dict[str, bytes | float | None] = {}
    for fasta in read_multiple(raw):
        percent = compute_gc_content(fasta["value"])
        if b < percent:
            b = percent
            max_fasta["name"] = fasta["name"]
            max_fasta["percent"] = percent

    return max_fasta


def compute_gc_content(dna: bytes | None) -> float:
    """Calculate GC content percentage in a DNA sequence.

    GC content is the percentage of Guanine (G) and Cytosine (C) bases
    in a DNA sequence. Important for determining DNA stability
    (GC bonds are stronger than AT bonds).

    Args:
        dna: DNA sequence as bytes, or None

    Returns:
        GC percentage (0.0 to 100.0)

    Example:
        >>> compute_gc_content(b"ATCG")
        50.0
        >>> compute_gc_content(b"AAAA")
        0.0
    """

    if dna is None:
        return 0.0

    count: dict[int, int] = do_counting(dna)

    return (count.get(ord("G"), 0) + count.get(ord("C"), 0)) * 100 / len(dna)
