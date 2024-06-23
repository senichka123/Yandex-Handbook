N = int(input())

toes = {}
for _ in range(N):
    txt = input()
    txt = txt.replace(':', '')
    txt = txt.replace(',', '')

    words = txt.split()
    del words[0]
    
    for each in set(words):
        toes[each] = toes.get(each, 0) + 1

for each in sorted(toes):
    if toes[each] == 1:
        print(each)