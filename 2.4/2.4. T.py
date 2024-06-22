N = int(input())

best_s = 0
best_i = 0

for i in range(2, 11):
    S = 0
    j = 0
    M = N
    while M > 0:
        S += (M % i)
        M //= i 
    if S > best_s:
        best_s = S
        best_i = i

print(best_i)