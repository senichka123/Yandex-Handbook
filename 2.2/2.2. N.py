N = int(input())

a = N // 100
b = N // 10 % 10
c = N % 10

if a == 0 and b == 0 or a == 0 and c == 0 or b == 0 and c == 0:
    N1 = max(a, b, c) * 10
    N2 = N1
elif a == 0 or b == 0 or c == 0:
    massive = [a, b, c]
    massive.remove(0)
    N1 = str(min(massive) * 10)
    N2 = max(massive) * 10 + min(massive)
else:
    massive = [a, b, c]
    massive.remove(max(a, b, c))
    N1 = min(massive) * 10 + max(massive)

    massive = [a, b, c]
    massive.remove(min(a, b, c))
    N2 = max(massive) * 10 + min(massive)

print(str(N1) + ' ' + str(N2))