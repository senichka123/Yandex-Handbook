X = 0
Y = 0

while (name := input()) != 'СТОП':
    N = int(input())
    if name == 'СЕВЕР':
        Y += N
    if name == 'ЮГ':
        Y -= N
    if name == 'ЗАПАД':
        X -= N
    if name == 'ВОСТОК':
        X += N

print(Y)
print(X)