N = int(input())

names = []
for i in range(N):
    names.append(input())

first = names[0]
for each in names:
    if each < first:
        first = each

print(first)