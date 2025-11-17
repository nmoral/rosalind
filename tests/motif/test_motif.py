def test_find_motif() -> None:
    from rosalind.motif.motif import find_motif

    assert find_motif(b"GATATATGCATATACTT", b"ATAT") == [2, 4, 10]


def test_kmp() -> None:
    from rosalind.motif.motif import kmp

    assert kmp(b"GATATATGCATATACTT", b"ATAT") == [2, 4, 10]


def test_kmp_table() -> None:
    from rosalind.motif.motif import kmp_table

    assert kmp_table(b"ABCDABD") == [-1, 0, 0, 0, -1, 0, 2, 0]
