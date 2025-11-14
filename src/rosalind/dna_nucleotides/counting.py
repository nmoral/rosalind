def counting(dna: bytes) -> str:
    """Retourne le comptage attendu des nucléotides pour le test de sanity.

    Nota: Ce kata évoluera probablement ensuite pour calculer à partir d'une
    séquence donnée; pour l'instant, on retourne simplement la chaîne attendue
    par le test minimal.
    """

    count = do_counting(dna)

    return (
        f"{count.get(ord('A'), 0)} "
        f"{count.get(ord('C'), 0)} "
        f"{count.get(ord('G'), 0)} "
        f"{count.get(ord('T'), 0)}"
    )


def do_counting(dna: bytes) -> dict[int, int]:
    count: dict[int, int] = {}

    for n in dna:
        count[n] = count.get(n, 0) + 1
    return count
