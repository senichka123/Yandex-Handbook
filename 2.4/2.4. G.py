N = int(input())

for i in range(1, N + 1):
    for k in range(i + 2, -1, -1):
        if k != 0:
            print(f'До старта {k} секунд(ы)')
        else:
            print(f'Старт {i}!!!')