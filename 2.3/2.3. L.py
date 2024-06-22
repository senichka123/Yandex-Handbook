N = int(input())

max_number = 0
while N != 0:
    max_number = max(max_number, N % 10)
    N //= 10

print(max_number)