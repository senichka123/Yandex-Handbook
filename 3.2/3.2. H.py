N = int(input())

s = dict()
for _ in range(N):
    txt = input().split()
    for k in range(1, len(txt)):
        if txt[k] not in s:
            s[txt[k]] = [txt[0]]
        else:
            s[txt[k]].append(txt[0])

kasha = input()

if kasha not in s:
    print('Таких нет')
else:
    for each in sorted(s[kasha]):
        print(each)