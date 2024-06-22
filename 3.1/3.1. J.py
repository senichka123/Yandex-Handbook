str_concat = ''

max_count = 0
max_symbol = ''

while (txt := input()) != 'ФИНИШ':
    str_concat += txt.lower()

str_concat = str_concat.replace(' ', '')

for char in str_concat:
    if str_concat.count(char) > max_count:
        max_count = str_concat.count(char)
        max_symbol = char
    elif str_concat.count(char) == max_count:
        if char < max_symbol:
            max_symbol = char

print(max_symbol)