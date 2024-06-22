massive = list(map(int, input()))

count = 0
for i in range(len(massive)):
    if (i + 1) != len(massive) and massive[i] == massive[i + 1]:
        count += 1
    else:
        count += 1
        print(f'{massive[i]} {count}')
        count = 0