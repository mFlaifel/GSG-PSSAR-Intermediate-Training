def mystery(n):
    if n <= 1:
        return 1
    return n * mystery(n - 1)


print(mystery(5))
