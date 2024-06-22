N = int(input())

massive = []
for i in range(N):
    massive.append(input())
S = 0
for each in massive:
    for symbols in each:
        S += int(symbols)
        
print(S)