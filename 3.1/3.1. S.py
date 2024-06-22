massive = input().split()

stack = []
while massive != []:
    x = massive.pop(0)
    if x not in ('+', '-', '*'):
        stack.append(int(x))
    elif x == '+':
        stack.append(stack.pop(-2) + stack.pop(-1))
    elif x == '-':
        stack.append(stack.pop(-2) - stack.pop(-1))
    elif x == '*':
        stack.append(stack.pop(-2) * stack.pop(-1))

print(stack[0])