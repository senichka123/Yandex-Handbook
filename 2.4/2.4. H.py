N = int(input())

winner = ''
summa = 0

for i in range(N):
    name = input()
    number = input()
    
    S = 0
    for symbols in number:
        S += int(symbols)
    if S >= summa:
        summa = S
        winner = name

print(winner)