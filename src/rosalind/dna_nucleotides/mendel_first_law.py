def compute_mendel_first_law(
    homozygous_dominant: int, heterozygous: int, homozygous_recessive: int
) -> float:
    population: int = homozygous_dominant + heterozygous + homozygous_recessive

    probability_punnett_heterozygous = 0.75
    probability_punnett_homozygous = 1
    probability_punnett_homozygous_heterozygous = 1
    probability_punnett_homozygous_recessive = 1
    probability_punnett_heterozygous_recessive = 0.5

    return (
        probability_with_same_genotype(homozygous_dominant, population)
        * probability_punnett_homozygous
        + probability_with_same_genotype(heterozygous, population)
        * probability_punnett_heterozygous
        + probability_with_different_genotype(
            homozygous_dominant, heterozygous, population
        )
        * probability_punnett_homozygous_heterozygous
        + probability_with_different_genotype(
            homozygous_dominant, homozygous_recessive, population
        )
        * probability_punnett_homozygous_recessive
        + probability_with_different_genotype(
            heterozygous, homozygous_recessive, population
        )
        * probability_punnett_heterozygous_recessive
    )


def probability_with_same_genotype(
    genotype_population_size: int, total_population: int
) -> float:
    return (genotype_population_size / total_population) * (
        (genotype_population_size - 1) / (total_population - 1)
    )


def probability_with_different_genotype(
    first_genotype_population_size: int,
    second_genotype_population_size: int,
    total_population: int,
) -> float:
    return (
        2
        * (first_genotype_population_size * second_genotype_population_size)
        / (total_population * (total_population - 1))
    )
