N = int(input())
M = int(input())

P = 7
V = 6

P = P - 3
V = V + 3
P = P + 2
P = P + N
V = V + M

if P > V:
    print('Петя')
else:
    print('Вася')