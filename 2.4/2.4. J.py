N = int(input())

print('А Б В')
for i in range(1, N - 1):
    for j in range(1, N - 1):
        for k in range(1, N - 1):
            if i + j + k == N:
                print(f'{i} {j} {k}')