massive = list(map(int, input().split()))

answer = []
for each in massive:
    s = {}
    binary = bin(each)[2:]
    s['digits'] = len(binary)
    s['units'] = binary.count('1')
    s['zeros'] = binary.count('0')
    answer.append(s)

print(answer)