massive = list(map(int, input().split()))

flag = 0
max_nod = 1

if len(massive) == 1:
    print(massive[0])
else:
    for i in range(2, max(massive) + 1):
        for each in massive:
            if each % i == 0 and flag != 1:
                flag = 0
                continue
            else:
                flag = 1
        if flag == 1:
            pass
        else:
            if i > max_nod:
                max_nod = i
        flag = 0

    print(max_nod)