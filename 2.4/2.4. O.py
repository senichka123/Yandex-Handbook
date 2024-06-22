N = int(input())
M = int(input())

k = len(str(N * M))

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if j % 2 == 1:
            txt = (j - 1) * N + i
        else:
            txt = j * N - i + 1
        print(f'{txt: >{k}}', end=' ')
    print('')