def counting_mutations(s: bytes, t: bytes) -> int:
    count = 0
    for i in range(len(s)):
        count = count + 1 if s[i] != t[i] else count

    return count
