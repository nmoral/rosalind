def read(raw: bytes) -> dict[str, bytes | None]:
    fasta: dict[str, bytes | None] = {"name": None, "value": None}

    part = [line.strip() for line in raw.splitlines() if line.strip()]

    fasta["name"] = part[0].replace(b">", b"")
    fasta["value"] = b"".join(part[1::])

    return fasta


def read_multiple(raw: bytes) -> list[dict[str, bytes | None]]:
    return [read(fasta) for fasta in raw.split(b">") if fasta.strip()]
