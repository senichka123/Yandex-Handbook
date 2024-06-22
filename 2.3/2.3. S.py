ask = 500
delta = ask // 2

txt = ''

while txt != 'Угадал!':
    print(ask)
    txt = input()
    if txt == 'Меньше':
        ask -= delta
    else:
        ask += delta
    if delta >= 2:
        delta = (delta + 1) // 2