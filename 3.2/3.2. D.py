N = int(input())
M = int(input())

a = []
b = []

for _ in range(N):
    a.append(input())

for _ in range(M):
    b.append(input())

count = 0
for each in set(a):
    if each in set(b):
        count += 1

if count == 0:
    print('Таких нет')
else:
    print(count)