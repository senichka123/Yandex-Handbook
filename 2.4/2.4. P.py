N = int(input())
M = int(input())

if M != 0:
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            print(f'{i * j: ^{M}}', end='')
            if j != N:
                print('|', end='')
            elif i != N:
                print('')
                for k in range(N * M + N - 1):
                    print('-', end='')
                print('')
else:
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            print(f'{i * j: ^{M}}', end='')
            if j != N:
                print('|', end='')
            elif i != N:
                print('')
                for k in range(N + N - 1):
                    print('-', end='')
                print('')