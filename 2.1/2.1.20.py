N = int(input())
M = int(input())
K1 = int(input())
K2 = int(input())

W1 = (N * M - N * K2) / (K1 - K2)
W2 = N - W1

print(str(int(W1)) + ' ' + str(int(W2)))