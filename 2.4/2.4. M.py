N = int(input())
M = int(input())

k = len(str(N * M))
for j in range(1, N + 1):
    for i in range(1, N * M + 1):
        if i % N == j:
            print(f'{i: >{k}} ', end='')
    if j != N:
        print('')

for i in range(1, N * M + 1):
    if i % N == 0:
        print(f'{i: >{k}} ', end='')