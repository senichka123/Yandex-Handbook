while (txt := input()) != '':
    if txt[-3:] == '@@@':
        continue
    elif txt[:2] == '##':
        print(txt[2:])
    else:
        print(txt)