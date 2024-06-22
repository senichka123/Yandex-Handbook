N = int(input())

count = 0
for i in range(N):
    txt = input()
    count += txt.count('зайка')

print(count)