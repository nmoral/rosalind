"""Tests for GC content computations (GC)."""


def test_compute_gc_content() -> None:
    """Compute GC% for a single DNA sequence."""
    from rosalind.dna_nucleotides.gc_content import compute_gc_content

    assert (
        abs(
            compute_gc_content(
                b"CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT"
            )
            - 60.919540
        )
        < 0.001
    )


def test_gc_content() -> None:
    """Find the sequence with the highest GC% from FASTA content."""
    from rosalind.dna_nucleotides.gc_content import gc_content

    assert (
        gc_content(b""">Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT""")
        == """Rosalind_0808
60.919540
"""
    )
