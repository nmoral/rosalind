"""Tests for transcribing DNA to RNA (RNA)."""


def test_transcribe() -> None:
    """Transcribe DNA into RNA and handle empty string input."""
    from rosalind.dna_nucleotides.transcribe import transcribe

    assert transcribe("GATGGAACTTGACTACGTAAATT") == "GAUGGAACUUGACUACGUAAAUU"
    assert transcribe("") == ""
