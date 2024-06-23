N = int(input())
T = {}

for _ in range(N):
    x, y = input().split()
    key = (int(x) // 10, int(y) // 10)
    T[key] = T.get(key, 0) + 1

print(max(T.values()))