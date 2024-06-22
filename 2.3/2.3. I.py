N = int(input())

F = 1
if N == 0:
    pass
else:
    for i in range(1, N + 1, 1):
        F = F * i

print(F)