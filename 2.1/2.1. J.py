name = input()
N = int(input())

a1 = N // 100
a2 = N // 10 % 10
a3 = N % 10

print(f'Группа №{a1}.')
print(f'{a3}. {name}.')
print(f'Шкафчик: {N}.')
print(f'Кроватка: {a2}.')
