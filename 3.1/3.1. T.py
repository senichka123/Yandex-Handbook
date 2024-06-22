import math

massive = input().split()

stack = []
while massive != []:
    x = massive.pop(0)
    if x not in ('+', '-', '*', '/', '~', '!', '#', '@'):
        stack.append(int(x))
    else:
        match x:
            case '+':
                stack.append(stack.pop(-2) + stack.pop(-1))
            case '-':
                stack.append(stack.pop(-2) - stack.pop(-1))
            case '*':
                stack.append(stack.pop(-2) * stack.pop(-1))
            case '/':
                stack.append(stack.pop(-2) // stack.pop(-1))
            case '~':            
                stack.append(-1 * stack.pop(-1))
            case '!':
                stack.append(math.factorial(stack.pop(-1)))
            case '#':
                double = stack.pop(-1)
                stack.append(double)
                stack.append(double)
            case '@':
                third = stack.pop()
                second = stack.pop()
                first = stack.pop()
                stack.append(second)
                stack.append(third)
                stack.append(first)
print(stack[0])