chains = {}

while (txt := input()) != '':
    names = txt.split()
    chains[names[0]] = chains.get(names[0], []) + [names[1]]
    chains[names[1]] = chains.get(names[1], []) + [names[0]]

answer = {}
for each in sorted(chains):
    level_1 = set(chains[each])
    level_2 = set()
    print(f'{each}: ', end='')
    for ppl in level_1:
        for x in chains[ppl]:
            if x not in level_1 and x != each:
                level_2.add(x)

    if len(level_2) == 0:
        print()
    else:
        level_2 = sorted(list(level_2))
        for k in range(len(level_2)):
            if k != len(level_2) - 1:
                print(f'{level_2[k]}', end=', ')
            else:
                print(f'{level_2[k]}')