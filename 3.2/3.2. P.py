set_of_seen_objects = set()

while (name := input()) != '':
    if 'зайка' in name:
        words = name.split()
        for i in range(len(words)):
            if words[i] == 'зайка':
                if len(words) == 1:
                    pass
                elif i == 0:
                    set_of_seen_objects.add(words[i + 1])
                elif i == len(words) - 1:
                    set_of_seen_objects.add(words[i - 1])
                else:
                    set_of_seen_objects.add(words[i - 1])
                    set_of_seen_objects.add(words[i + 1])

for each in set_of_seen_objects:
    print(each)