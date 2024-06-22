N = int(input())
text = str(N)

symbols_to_remove = "02468"
 
for symbol in symbols_to_remove:
    text = text.replace(symbol, "")

print(text)