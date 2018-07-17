from Deque import Deque

def isPalindrome(str):
    word = Deque()
    for ch in str:
        word.addFront(ch)

    while  word.size() > 1:
        if word.removeFront() != word.removeRear():
            return False

    return True


if __name__ == '__main__':
    print(isPalindrome("radar"))
    print(isPalindrome("lsdkjfskf"))
