while (name := input()) != '':
    if name[0] == '#':
        pass
    else:
        if '#' in name:
            print(name[:name.index('#')])
        else:
            print(name)