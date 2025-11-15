def test_rna_to_protein() -> None:
    from rosalind.dna_nucleotides.codon import rna_to_protein

    assert (
        rna_to_protein(b"AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA")
        == b"MAMAPRTEINSTRING"
    )
    assert rna_to_protein(b"AUGUAA") == b"M"
    assert rna_to_protein(b"AUGUGGCAUUAG") == b"MWH"
    assert rna_to_protein(b"AUGUGGCAUUGA") == b"MWH"
    assert rna_to_protein(b"AUGGUACAUGCAUUUCCCAAAUAA") == b"MVHAFPK"
    assert rna_to_protein(b"AUGUUUUUCUAUUACUGGUGGUGA") == b"MFFYYWW"
    assert (
        rna_to_protein(b"AUGUGGGCACCCGAAGCUAGUAAAUUCGACGGCCAUUGUUAA")
        == b"MWAPEASKFDGHC"
    )
