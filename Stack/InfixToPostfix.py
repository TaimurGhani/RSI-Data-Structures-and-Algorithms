from StackOne import Stack

def infixToPostfix(infix):
    pres = {}
    pres['**'] = 4
    pres['*'] = 3
    pres['/'] = 3
    pres['+'] = 2
    pres['-'] = 2
    pres['('] = 1

    opStack = Stack()
    postfix = []
    tokens = infix.split()

    for elem in tokens:
        if elem in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or elem in "0123456789":
            postfix.append(elem)
        elif elem == "(":
            opStack.push("(")
        elif elem == ")":
            while (opStack.peek() != "("):
                postfix.append(opStack.pop())
            opStack.pop()
        else:
            if opStack.isEmpty():
                opStack.push(elem)
            else:
                if (pres[elem] >= pres[opStack.peek()]):
                    opStack.push(elem)
                else:
                    postfix.append(opStack.pop())
                    opStack.push(elem)

    while not opStack.isEmpty():
        postfix.append(opStack.pop())

    return " ".join(postfix)


if __name__ == '__main__':
    print(infixToPostfix("A * B + C * D"))
    print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
    print(infixToPostfix("( A + B ) * ( C + D )"))
    print(infixToPostfix("( A + B ) * C"))
    print(infixToPostfix("A + B * C"))
    print(infixToPostfix("5 * 3 ** ( 4 - 2 )"))