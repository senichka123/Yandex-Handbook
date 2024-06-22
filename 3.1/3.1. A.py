N = int(input())

massive = []
for i in range(N):
    massive.append(input())

flag = 0
for each in massive:
    if each[0] in ('а', 'б', 'в'):
        continue
    else:
        flag = 1
        print('NO')
        break

if flag == 0:
    print('YES')