N = int(input())

massive = []
count = 0

for i in range(N):
    massive.append(input())

for each in massive:
    if len(each) == 1:
        count += 1
    elif len(each) % 2 == 0:
        if each[:int(len(each) / 2)] == each[int(len(each) / 2): int(len(each))][::-1]:
            count += 1
    else:
        if each[:int(len(each) / 2)] == each[int(len(each) / 2) + 1: int(len(each))][::-1]:
            count += 1

print(count)