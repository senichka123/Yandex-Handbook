N = int(input())

a1 = N // 1000
a2 = N // 100 % 10
a3 = N // 10 % 10
a4 = N % 10

N = a2 * 1000 + a1 * 100 + a4 * 10 + a3
print(N)