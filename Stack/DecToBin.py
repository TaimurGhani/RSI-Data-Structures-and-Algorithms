from StackOne import Stack

def decToBin(num):
    s = Stack()
    while (num != 0):
        s.push(num % 2)
        num = num//2
    result = ""
    while (not s.isEmpty()):
        result += str(s.pop())
    return result


print(decToBin(42))