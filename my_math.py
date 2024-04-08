def factorial(n):
    if n == 1:
        return n
    return n * factorial(n - 1)


def degree_of(num, deg):
    res = num ** deg
    return res


# print(factorial(3))
# print(degree_of(4, 2))
