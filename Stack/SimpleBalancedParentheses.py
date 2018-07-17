from StackOne import Stack

def parChecker(symbolString):
    s = Stack()
    for paren in symbolString:
        if paren == '(':
            s.push('(')
        elif paren == ')':
            if (s.isEmpty()):
                return False
            else:
                s.pop()
    if s.isEmpty():
        return True
    else:
        return False

if __name__ == '__main__':
    print(parChecker('((()))'))
    print(parChecker('(()'))