N = int(input())

massive = []
for _ in range(N):
    txt = input().split()
    for each in txt:
        massive.append(each)

for each in set(massive):
    print(each)