N = int(input())

a = N // 100
b = N // 10 % 10
c = N % 10

max_numb = max(a, b, c)
min_numb = min(a, b, c)
if a != min_numb and a != max_numb:
    mid_numb = a
elif b != min_numb and b != max_numb:
    mid_numb = b
else:
    mid_numb = c
if min_numb + max_numb == mid_numb * 2:
    print('YES')
else:
    print('NO')