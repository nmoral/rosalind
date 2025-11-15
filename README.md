# Rosalind Bioinformatics Solutions

Personal solutions to algorithmic problems from [Rosalind.info](http://rosalind.info/) as part of my career transition to bioinformatics.

## Purpose

This repository is a learning space where I:
- Practice fundamental bioinformatics algorithms
- Learn Python for biological sequence manipulation
- Build a foundation for future open-source contributions

## Installation

```bash
# Clone the repository
git clone [URL]

# Install in development mode
pip install -e .

# Run tests
pytest
```

## Structure

```
src/rosalind/
├── dna_nucleotides/    # DNA/RNA sequence problems
├── fasta/              # FASTA format parser
└── ...                 # More to come
```

## Solved Problems

### Bioinformatics Stronghold
- [x] **DNA** - Counting DNA Nucleotides
- [x] **RNA** - Transcribing DNA into RNA
- [x] **REVC** - Complementing a Strand of DNA
- [x] **HAMM** - Counting Point Mutations
- [x] **FIB** - Rabbits and Recurrence Relations
- [x] **GC** - Computing GC Content

## Usage Example

```python
from rosalind.dna_nucleotides.counting import counting

sequence = b"AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
result = counting(sequence)
print(result)  # Output: "20 12 17 21"
```

## Resources

- [Rosalind.info](http://rosalind.info/) - Problem platform
- [My biology notes](link-to-notes-repo) - Molecular biology revision notes
- [Bioinformatics Algorithms](http://bioinformaticsalgorithms.com/) - Reference book

## About

Nicolas - Backend developer transitioning to bioinformatics
