N = int(input())

massive = []
for i in range(N):
    massive.append(input())

answer = 0
for k in range(len(massive)):
    max_symbol = 0
    for symbol in massive[k]:
        if int(symbol) >= max_symbol:
            max_symbol = int(symbol)
    answer += max_symbol * 10 ** (N - k - 1)

print(answer)