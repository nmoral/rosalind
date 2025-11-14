def complementing(dna: bytes) -> bytes:
    return dna.translate(bytes.maketrans(b"ATCG", b"TAGC"))[::-1]
