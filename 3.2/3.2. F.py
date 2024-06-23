N = int(input())
M = int(input())

a = []

for _ in range(N + M):
    if (name := input()) not in a:
        a.append(name)
    else:
        a.remove(name)

count = len(set(a))
if count == 0:
    print('Таких нет')
else:
    for each in sorted(set(a)):
        print(each)