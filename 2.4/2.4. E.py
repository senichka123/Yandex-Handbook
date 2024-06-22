N = int(input())

count = 0
flag = 0

for i in range(N):
    while (name := input()) != 'ВСЁ':
        if name == 'зайка' and flag == 0:
            count += 1
            flag = 1
    flag = 0

print(count)