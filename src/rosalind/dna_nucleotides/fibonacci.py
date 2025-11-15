def fibonacci(n: int, k: int) -> int:
    """Calculate rabbit population using modified Fibonacci sequence.

    In the Fibonacci Rabbits problem:
    - Each generation, a mature pair produces k new pairs
    - F(n) = F(n-1) + k * F(n-2)
    - F(1) = F(2) = 1 (initial conditions)

    Args:
        n: Number of months (generations)
        k: Number of pairs produced by each mature pair

    Returns:
        Total number of rabbit pairs after n months

    Example:
        >>> fibonacci(5, 3)
        19
        >>> fibonacci(6, 3)
        40

    Note:
        Iterative implementation: O(n) time, O(1) space
    """
    if n <= 1:
        return 1
    a, b = 1, 1
    for _ in range(3, n + 1):
        a, b = b, b + k * a

    return b
