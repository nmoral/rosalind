def test_transcribe() -> None:
    from rosalind.dna_nucleotides.transcribe import transcribe

    assert transcribe("GATGGAACTTGACTACGTAAATT") == "GAUGGAACUUGACUACGUAAAUU"
    assert transcribe("") == ""
