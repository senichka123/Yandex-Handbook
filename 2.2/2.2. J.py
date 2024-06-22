N = int(input())

a = N // 100
b = N // 10 % 10
c = N % 10

N1 = b + c
N2 = a + b

if N1 > N2:
    print(str(N1) + str(N2))
else:
    print(str(N2) + str(N1))