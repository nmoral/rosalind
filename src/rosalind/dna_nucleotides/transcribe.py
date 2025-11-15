def transcribe(dna: str) -> str:
    """Transcribe a DNA sequence to RNA.

    Replaces all thymine (T) with uracil (U).
    DNA uses ATCG, RNA uses AUCG.

    Args:
        dna: DNA sequence as string (e.g., "ATCG")

    Returns:
        RNA sequence as string (e.g., "AUCG")

    Example:
        >>> transcribe("GATGGAACTTGACTACGTAAATT")
        'GAUGGAACUUGACUACGUAAAUU'
    """
    return dna.translate(str.maketrans("T", "U"))
