from StackOne import Stack

def baseConverter(decNumber, base):
    digits = "0123456789ABCDE"
    s = Stack()
    while (decNumber != 0):
        remainder = decNumber % base
        s.push(digits[remainder])
        decNumber = decNumber // base
    result = ""
    while not s.isEmpty():
        result += s.pop()
    return result

if __name__ == '__main__':
    print(baseConverter(25, 8))
    print(baseConverter(26, 26))
