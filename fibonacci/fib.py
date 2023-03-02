def fib(n: int):
    a, b = 1, 1
    for _ in range(n):
        a, b = a+b, a
    return a
