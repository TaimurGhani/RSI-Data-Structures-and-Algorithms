from StackOne import Stack

def parChecker(symbolString):
    s = Stack()
    open = ['(', '{', '[']
    close = [')', '}', ']']
    for paren in symbolString:
        if paren in open:
            s.push(paren)
        else:
            if (s.isEmpty()):
                return False
            else:
                if close.index(paren) == open.index(s.peek()):
                    s.pop()
                else:
                    return False
    if s.isEmpty():
        return True
    else:
        return False

if __name__ == '__main__':
    print(parChecker('{{([][])}()}'))
    print(parChecker('[{()]'))