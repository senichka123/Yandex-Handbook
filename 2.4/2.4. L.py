N = int(input())
M = int(input())

k = len(str(N * M))

for i in range(1, N + 1):
    for j in range(1, M + 1):
        print(f'{M * (i - 1) + j: >{k}} ', end='')
        if j % M == 0:
            print('')