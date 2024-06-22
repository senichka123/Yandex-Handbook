L = int(input())
N = int(input())

massive = []
title = ''

for _ in range(N):
    txt = input()
    massive.append(txt)
    title += txt

length_title = len(title)
length_print = L - 3

if L == 1:
    print('.')
elif L == 2:
    print('..')
elif L == 3:
    print('...')
elif length_title >= 3:
    for each in massive:
        if length_print <= 0:
            break
        if len(each) < length_print:
            print(each)
            length_print -= len(each)
        else:
            print(each[:length_print] + '...')
            length_print -= len(each)
else:
    for each in massive:
        print(each)