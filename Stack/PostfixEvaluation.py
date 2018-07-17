from StackOne import Stack

def postfixEval(postfixExpr):
    resStack = Stack()
    tokens = postfixExpr.split()

    for elem in tokens:
        if elem in "0123456789":
            resStack.push(int(elem))
        else:
            second = resStack.pop()
            first = resStack.pop()
            resStack.push(doMath(elem, first, second))
    return int(resStack.pop())



def doMath(operator, operand1, operand2):
    if operator == "*":
        return operand1 * operand2
    elif operator == "/":
        return operand1 / operand2
    elif operator == "+":
        return operand1 + operand2
    else:
        return operand1 - operand2

if __name__ == '__main__':
    print(postfixEval('7 8 + 3 2 + /'))