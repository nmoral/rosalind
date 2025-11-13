def transcribe(dna: str) -> str:
    return dna.translate(str.maketrans("T", "U"))
