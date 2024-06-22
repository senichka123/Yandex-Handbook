v1 = int(input())
v2 = int(input())
v3 = int(input())

if v1 > v2 and v1 > v3:
    print(f'{"Петя": ^24}')
    if v2 > v3:
        print(f'{"Вася": ^8}')
        print(f'{"": >16}' + f'{"Толя": ^8}')
    else:
        print(f'{"Толя": ^8}')
        print(f'{"": >16}' + f'{"Вася": ^8}')
elif v2 > v1 and v2 > v3:
    print(f'{"Вася": ^24}')
    if v1 > v3:
        print(f'{"Петя": ^8}')
        print(f'{"": >16}' + f'{"Толя": ^8}')
    else:
        print(f'{"Толя": ^8}')
        print(f'{"": >16}' + f'{"Петя": ^8}')
else:
    print(f'{"Толя": ^24}')
    if v1 > v2:
        print(f'{"Петя": ^8}')
        print(f'{"": >16}' + f'{"Вася": ^8}')
    else:
        print(f'{"Вася": ^8}')
        print(f'{"": >16}' + f'{"Петя": ^8}')
        
print(f'{"II": ^8}' + f'{"I": ^8}' + f'{"III": ^8}')