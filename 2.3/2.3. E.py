S = 0

while (price := float(input())) != 0:
    if price >= 500:
        price = price * 0.9
    S += price

print(S)
