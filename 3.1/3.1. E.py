txt = input()

if len(txt) % 2 == 0:
    if txt[:int(len(txt) / 2)] == txt[int(len(txt) / 2):][::-1]:
        print('YES')
    else:
        print('NO')
else:
    if txt[:int(len(txt) / 2)] == txt[int(len(txt) / 2) + 1:][::-1]:
        print('YES')
    else:
        print('NO')