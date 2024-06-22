a = int(input())

ind = 0

if a == 1:
    print('NO')
    ind = 1
else:
    for i in range(2, int(a / 2) + 1, 1):
        if a % i == 0:
            print('NO')
            ind = 1
            break

if ind == 0:
    print('YES')