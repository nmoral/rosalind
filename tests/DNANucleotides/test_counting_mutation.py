def test_counting_mutations() -> None:
    from rosalind.dna_nucleotides.counting_mutation import counting_mutations

    assert (
        counting_mutations(
            b"GAGCCTACTAACGGGAT",
            b"CATCGTAATGACGGCCT",
        )
        == 7
    )

    assert (
        counting_mutations(
            b"ATCG",
            b"ATCG",
        )
        == 0
    )

    assert (
        counting_mutations(
            b"AAAAAAAAAA",
            b"ATATATATAT",
        )
        == 5
    )

    assert (
        counting_mutations(
            b"GCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAG",
            b"GCTAGCTGGCTAGCTAGCTAGGTAGCTAGCTAGCTCGCTAGCTAGCTAG",
        )
        == 3
    )

    assert (
        counting_mutations(
            b"AAAAAAA",
            b"TTTTTTT",
        )
        == 7
    )

    assert (
        counting_mutations(
            b"ATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGC",
            b"ATGCATGCATCCATGCATGGATGCATGCATGCCTGCATGCATGCATGCAGGCATGCATGCATGCATGGATGCATGCTTGCATGCATGCATGCATGC",
        )
        == 66
    )
