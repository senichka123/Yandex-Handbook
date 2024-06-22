N = int(input())

width = len(str((N + 1) // 2))
if N == 0:
    pass
else:
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i == j:
                if i < (N + 1) / 2:
                    print(f'{i: >{width}} ', end='')
                else:
                    print(f'{N - i + 1: >{width}} ', end='')
            else:
                print(f'{min(i, j, N - i + 1, N - j + 1): >{width}} ', end='')
        if i != N:
            print('')