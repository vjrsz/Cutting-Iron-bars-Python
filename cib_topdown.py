global B, S


def cib_topdown(n, p):
    global B, S
    B = [-1] * (n + 1)
    S = [-1] * (n + 1)

    B[0] = 0

    return cib_recursive_topdown(n, p)


def cib_recursive_topdown(k, p):
    if B[k] == -1:
        profit = -1
        for i in range(1, k):
            value = p[i] + cib_recursive_topdown(k - i, p)
            if value > profit:
                profit = value
                S[k] = i
        B[k] = profit

    return B[k]
