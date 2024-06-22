N = int(input())

massive = []
for i in range(N):
    massive.append(int(input()))

count = 0
for each in massive:
    ind = 0

    if each == 1:
        ind = 1
    else:
        for i in range(2, int(each / 2) + 1, 1):
            if each % i == 0:
                ind = 1
                break
    if ind == 0:
        count += 1

print(count)