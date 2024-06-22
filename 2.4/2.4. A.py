N = int(input())

for i in range(1, N + 1):
    for k in range(1, N + 1):
        print(k * i, end=' ')
    print('\n', end='')