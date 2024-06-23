N = int(input())

s = dict()
for _ in range(N):
    name = input()
    s[name] = s.get(name, 0) + 1

flag = 0
for key in sorted(s):
    if s[key] != 1:
        flag = 1
        print(f'{key} - {s[key]}')

if flag == 0:
    print('Однофамильцев нет')