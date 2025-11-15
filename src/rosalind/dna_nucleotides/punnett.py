def generate_punnett(p1: str, p2: str) -> list[str]:
    return [p1[j] + p2[i] for i in range(len(p2)) for j in range(len(p1))]


def compute_punnett_probability(punnett_square: list[str], allele: str) -> float:
    length: int = len(punnett_square)
    count: int = 0

    for child in punnett_square:
        count = count + 1 if allele in child else count

    return count / length
