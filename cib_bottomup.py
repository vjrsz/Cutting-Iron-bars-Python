def cib_bottomup(n, p):
    B = [0] * (n + 1)
    S = [0] * (n + 1)

    for k in range(1, n + 1):
        profit = -1
        for i in range(1, k):
            value = p[i] + B[k - i]
            if value > profit:
                profit = value
                S[k] = i
        B[k] = profit

    return B[n]