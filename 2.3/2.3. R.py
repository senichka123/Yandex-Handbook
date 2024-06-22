N = int(input())


def Factor(n):
    Ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            Ans.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        Ans.append(n)
    return Ans


massive = Factor(N)
for i in range(len(massive)):
    print(massive[i], end='')
    if i != len(massive) - 1:
        print(' * ', end='')