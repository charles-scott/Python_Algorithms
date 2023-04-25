def fib(n, memo=None):
    """Compute the nth Fibonacci number."""
    if memo is None:
        memo = {1: 1, 2: 1}
    if n in memo:
        return memo[n]
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)

    return memo[n]


if __name__ == '__main__':
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    assert fib(5) == 5
    print(fib(50))
