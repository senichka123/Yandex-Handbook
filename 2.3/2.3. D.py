a = int(input())
b = int(input())

txt = ''

if a < b:
    for i in range(a, b + 1):
        txt = txt + str(i) + ' '
else:
    for i in range(a, b - 1, -1):
        txt = txt + str(i) + ' '

print(txt)