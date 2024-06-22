a = input()
b = input()
c = input()

massive = []
if 'зайка' in a:
    massive.append(a)
if 'зайка' in b:
    massive.append(b)
if 'зайка' in c:
    massive.append(c)

if len(massive) == 1:
    print(massive[0], len(massive[0]))
elif len(massive) == 2:
    if massive[0] <= massive[1]:
        print(massive[0], len(massive[0]))
    else:
        print(massive[1], len(massive[1]))
elif len(massive) == 3:
    if massive[0] <= massive[1] and massive[0] <= massive[2]:
        print(massive[0], len(massive[0]))
    elif massive[1] <= massive[0] and massive[1] <= massive[2]:
        print(massive[1], len(massive[1]))
    else:
        print(massive[2], len(massive[2]))