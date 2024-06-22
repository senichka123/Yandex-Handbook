N = int(input())

for i in range(N):
    txt = input()
    if 'зайка' in txt:
        print(txt.index('зайка') + 1)
    else:
        print('Заек нет =(')