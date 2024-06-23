s = dict()

while (name := input()) != '':
    words = name.split()
    for word in words:
        s[word] = s.get(word, 0) + 1

for key in s:
    print(f'{key} {s[key]}')