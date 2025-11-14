def fibonacci(n: int, k: int) -> int:
    """
    fibonacci is equal to Fn = Fn-1 + Fn-2

    with k, fibonacci is equal to Fn = Fn-1 + k * Fn-2

    1 1 4 7 19 40
    1 1 3 5 11 21
    """
    if n <= 1:
        return 1
    a, b = 1, 1
    for _ in range(3, n + 1):
        a, b = b, b + k * a

    return b
