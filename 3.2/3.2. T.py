numbers = list(map(int, input().replace(';', '').split()))
numbers = sorted(list(set(numbers)))

for i in range(len(numbers)):
    output = set()
    if numbers[i] == 1:
        for j in range(len(numbers)):
            if numbers[j] != 1:
                output.add(numbers[j])
    else:
        for j in range(len(numbers)):
            if numbers[j] == 1:
                output.add(numbers[j])
            if numbers[i] != numbers[j]:
                flag = 0
                for k in range(2, int(max(numbers[i], numbers[j]) / 2 + 1)):
                    if numbers[i] % k == 0 and numbers[j] % k == 0:
                        flag = 1
                if flag == 0:
                    output.add(numbers[j])
    output = sorted(list(output))
    if len(output) > 0:
        print(f'{numbers[i]} - ', end='')
        for z in range(len(output)):
            if z == len(output) - 1:
                print(f'{output[z]}')
            else:
                print(f'{output[z]}', end=', ')