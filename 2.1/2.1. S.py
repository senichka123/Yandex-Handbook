name = input()
price = int(input())
weight = int(input())
money = int(input())

print(f'{"Чек":=^35}')
print(f'Товар:' + f'{name: >29}')
txt = str(weight) + 'кг * ' + str(price) + 'руб/кг'
print(f'Цена:' + f'{txt: >30}')
print(f'Итого:' + f'{weight * price: >26}руб')
print(f'Внесено:' + f'{money: >24}руб')
print(f'Сдача:' + f'{money - weight * price: >26}руб')
print(f'{"":=^35}')
