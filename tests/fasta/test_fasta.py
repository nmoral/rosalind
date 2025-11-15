"""Tests for parsing FASTA format (FASTA)."""


def test_read() -> None:
    """Parse a single FASTA entry and join multi-line sequence."""
    from rosalind.fasta.fasta import read

    fasta: dict[str, bytes | None] = read(b""">Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
""")

    assert fasta["name"] == b"Rosalind_6404"
    assert (
        fasta["value"]
        == b"CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG"
    )


def test_read_with_empty_line() -> None:
    """Ignore empty lines while parsing a single FASTA entry."""
    from rosalind.fasta.fasta import read

    fasta: dict[str, bytes | None] = read(b"""
    >Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC

TCCCACTAATAATTCTGAGG

    """)

    assert fasta["name"] == b"Rosalind_6404"
    assert (
        fasta["value"]
        == b"CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG"
    )


def test_read_multiple() -> None:
    """Parse multiple FASTA entries from a single buffer."""
    from rosalind.fasta.fasta import read_multiple

    fasta: list[dict[str, bytes | None]] = read_multiple(b""">Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT""")

    assert fasta[0]["name"] == b"Rosalind_6404"
    assert (
        fasta[0]["value"]
        == b"CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG"
    )

    assert fasta[1]["name"] == b"Rosalind_5959"
    assert (
        fasta[1]["value"]
        == b"CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC"
    )

    assert fasta[2]["name"] == b"Rosalind_0808"
    assert (
        fasta[2]["value"]
        == b"CCACCCTCGTGGTATGGCTAGGCATTCAGG"
        + b"AACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT"
    )
