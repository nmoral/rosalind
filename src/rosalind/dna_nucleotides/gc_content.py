from rosalind.dna_nucleotides.counting import do_counting
from rosalind.fasta.fasta import read_multiple


def gc_content(dna_fasta: bytes) -> str:
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
    """
    pour une chaine de caractère CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGA
    GGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG
    retourne le pourcentage de GC dans l'ensemble
    :param dna:
    :return:
    """

    if dna is None:
        return 0.0

    count: dict[int, int] = do_counting(dna)

    return (count.get(ord("G"), 0) + count.get(ord("C"), 0)) * 100 / len(dna)
