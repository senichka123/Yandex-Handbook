N = int(input())

S = 0
while N != 0:
    S += N % 10
    N //= 10

print(S)