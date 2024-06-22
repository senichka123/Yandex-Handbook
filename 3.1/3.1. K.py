N = int(input())

massive = []
for i in range(N):
    massive.append(input())

search = input()

for title in massive:
    if search.lower() in title.lower():
        print(title)
    else:
        pass