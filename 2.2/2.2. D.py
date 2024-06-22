v1 = int(input())
v2 = int(input())
v3 = int(input())


if v1 > v2 and v1 > v3:
    print('1. Петя')
    if v2 > v3:
        print('2. Вася')
        print('3. Толя')
    else:
        print('2. Толя')
        print('3. Вася')
elif v2 > v1 and v2 > v3:
    print('1. Вася')
    if v1 > v3:
        print('2. Петя')
        print('3. Толя')
    else:
        print('2. Толя')
        print('3. Петя')
else:
    print('1. Толя')
    if v1 > v2:
        print('2. Петя')
        print('3. Вася')
    else:
        print('2. Вася')
        print('3. Петя')
