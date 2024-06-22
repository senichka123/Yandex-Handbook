N = int(input())

count = 0
for i in range(N):
    txt = input()
    if 'зайка' in txt:
        count += 1

print(count)