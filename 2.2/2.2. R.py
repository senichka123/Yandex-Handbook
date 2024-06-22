import math

a = int(input())
b = int(input())
c = int(input())

massive = [a, b, c]
massive = sorted(massive)

X = (-massive[2] ** 2 + massive[1] ** 2 + massive[0] ** 2) / (2 * massive[1] * massive[0])

if X < 0:
    print('велика')
elif X > 0:
    print('крайне мала')
else:
    print('100%')