a = int(input())
b = int(input())

a1 = a // 10
a2 = a % 10

b1 = b // 10
b2 = b % 10

massive = [a1, a2, b1, b2]

first = max(massive)
last = min(massive)

massive.remove(max(massive))
massive.remove(min(massive))

N = str(first) + str((massive[0] + massive[1]) % 10) + str(last)

print(N)