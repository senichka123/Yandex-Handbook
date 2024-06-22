N = int(input())

txt = str(N)
if len(txt) % 2 == 0:
    if txt[:int(len(txt) / 2)] == txt[int(len(txt) / 2):int(len(txt))][::-1]:
        print('YES')
    else:
        print('NO')
else:
    if txt[:int(len(txt) / 2)] == txt[int((len(txt) + 1) / 2):int(len(txt))][::-1]:
        print('YES')
    else:
        print('NO')