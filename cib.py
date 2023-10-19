def cib(n, p):
    if n == 0:
        return 0

    profit = -1

    for i in range(1, n):
        value = p[i] + cib(n - i, p)

        if value > profit:
            profit = value

    return profit


