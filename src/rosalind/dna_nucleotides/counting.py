def counting(dna: str) -> str:
    """Retourne le comptage attendu des nucléotides pour le test de sanity.

    Nota: Ce kata évoluera probablement ensuite pour calculer à partir d'une
    séquence donnée; pour l'instant, on retourne simplement la chaîne attendue
    par le test minimal.
    """

    compte: dict[str, int] = {}

    for n in dna:
        compte[n] = compte.get(n, 0) + 1

    return f"{compte.get('A', 0)} {compte.get('C', 0)} {compte.get('G', 0)} {compte.get('T', 0)}"
