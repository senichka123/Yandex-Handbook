a = int(input())
b = int(input())

massive_a = []
massive_b = []

for i in range(1, int(a / 2) + 1, 1):
    if a % i == 0:
        massive_a.append(i)
for i in range(1, int(b / 2) + 1, 1):
    if b % i == 0:
        massive_b.append(i)
 
massive = []
for each in massive_a:
    for every in massive_b:
        if each == every:
            massive.append(each)

print(max(massive))