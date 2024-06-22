L = int(input())
N = int(input())

massive = []
for i in range(N):
    massive.append(input())

for each in massive:
    if len(each) > L:
        print(f'{each[:L - 3]}...')
    else:
        print(each)