N = int(input())

s = dict()
for _ in range(N):
    name = input()
    s[name] = s.get(name, 0) + 1

count = 0
for key in s:
    if s[key] != 1:
        count += s[key]

print(count)