N = int(input())
b = 0
c = 1
 
for i in range(1, N + 1):
    if b != c:
        print(i, end=' ')
        b += 1
    else:
        print(f'\n{i}', end=' ')
        b = 1
        c += 1