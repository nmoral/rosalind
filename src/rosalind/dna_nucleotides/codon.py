def rna_to_protein(rna: bytes) -> bytes:
    protein: bytes = b""

    for i in range(0, len(rna), 3):
        codon: bytes = rna[i : i + 3]
        if len(codon) < 3:
            break
        amino: bytes = codon_to_amino_acid(codon)
        if amino == b"stop" or amino == b"unknown":
            break
        protein += amino

    return protein


def codon_to_amino_acid(codon: bytes) -> bytes:
    match codon:
        case b"UUU" | b"UUC":
            return b"F"
        case b"UUA" | b"UUG" | b"CUU" | b"CUC" | b"CUA" | b"CUG":
            return b"L"
        case b"UCU" | b"UCC" | b"UCA" | b"UCG" | b"AGU" | b"AGC":
            return b"S"
        case b"UAU" | b"UAC":
            return b"Y"
        case b"UGU" | b"UGC":
            return b"C"
        case b"UGG":
            return b"W"
        case b"CCU" | b"CCC" | b"CCA" | b"CCG":
            return b"P"
        case b"CAU" | b"CAC":
            return b"H"
        case b"CAA" | b"CAG":
            return b"Q"
        case b"CGU" | b"CGC" | b"CGA" | b"CGG" | b"AGA" | b"AGG":
            return b"R"
        case b"AUU" | b"AUC" | b"AUA":
            return b"I"
        case b"AUG":
            return b"M"
        case b"ACU" | b"ACC" | b"ACA" | b"ACG":
            return b"T"
        case b"AAU" | b"AAC":
            return b"N"
        case b"AAA" | b"AAG":
            return b"K"
        case b"GUU" | b"GUC" | b"GUA" | b"GUG":
            return b"V"
        case b"GCU" | b"GCC" | b"GCA" | b"GCG":
            return b"A"
        case b"GAU" | b"GAC":
            return b"D"
        case b"GAA" | b"GAG":
            return b"E"
        case b"GGU" | b"GGC" | b"GGA" | b"GGG":
            return b"G"
        case b"UAA" | b"UAG" | b"UGA":
            return b"stop"

    return b"UNKNOWN"
