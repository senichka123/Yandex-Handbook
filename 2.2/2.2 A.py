a = input()
b = input()

print('Как Вас зовут?')
print(f'Здравствуйте, {a}!')
print('Как дела?')
match b:
    case 'хорошо':
        print(f'Я за вас рада!')
    case 'плохо':
        print(f'Всё наладится!')