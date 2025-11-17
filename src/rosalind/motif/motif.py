def find_motif(dna: bytes, word: bytes) -> list[int]:
    dna_size: int = len(dna)
    motif_size: int = len(word)
    dna_index: int = 0
    motif_index: int
    position: list[int] = []
    while dna_index < dna_size:
        motif_index = 0
        while motif_index < motif_size:
            if (
                dna_index + motif_index >= dna_size
                or dna[dna_index + motif_index] != word[motif_index]
            ):
                break
            motif_index += 1
        if motif_index == motif_size:
            position.append(dna_index + 1)
        dna_index += 1

    return position


def kmp(dna: bytes, word: bytes) -> list[int]:
    table: list[int] = kmp_table(word)
    dna_length: int = len(dna)
    word_length: int = len(word)
    dna_index: int = 0
    word_index: int = 0
    position: list[int] = []

    while dna_index < dna_length:
        if word[word_index] == dna[dna_index]:
            dna_index += 1
            word_index += 1
            if word_index == word_length:
                position.append(dna_index - word_index + 1)
                word_index = table[word_index]
        else:
            word_index = table[word_index]
            if word_index < 0:
                dna_index += 1
                word_index += 1

    return position


def kmp_table(word: bytes) -> list[int]:
    word_index: int = 1

    word_length: int = len(word)
    next_candidate: int = 0
    table: list[int] = [-1]

    while word_index <= word_length:
        table.append(0)
        word_index += 1

    word_index = 1

    while word_index < word_length:
        if word[word_index] == word[next_candidate]:
            table[word_index] = table[next_candidate]
        else:
            table[word_index] = next_candidate
            while next_candidate >= 0 and word[word_index] != word[next_candidate]:
                next_candidate = table[next_candidate]
        word_index, next_candidate = word_index + 1, next_candidate + 1

    table[word_index] = next_candidate
    return table
