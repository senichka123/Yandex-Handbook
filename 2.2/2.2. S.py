X = float(input())
Y = float(input())

if X ** 2 + Y ** 2 > 100:
    print('Вы вышли в море и рискуете быть съеденным акулой!')
elif X >= 0 and Y >= 0:
    if X ** 2 + Y ** 2 <= 25:
        print('Опасность! Покиньте зону как можно скорее!')
    else:
        print('Зона безопасна. Продолжайте работу.')
elif X < 0 and Y > 0:
    if X >= -4 and Y <= 5:
        print('Опасность! Покиньте зону как можно скорее!')
    elif -7 <= X < -4 and Y <= 5 / 3 * X + 35 / 3:
        print('Опасность! Покиньте зону как можно скорее!')
    else:
        print('Зона безопасна. Продолжайте работу.')
elif Y < 0:
    if Y >= 1 / 4 * X ** 2 + 1 / 2 * X - 35 / 4:
        print('Опасность! Покиньте зону как можно скорее!')
    else:
        print('Зона безопасна. Продолжайте работу.')