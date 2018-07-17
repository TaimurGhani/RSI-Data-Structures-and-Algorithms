from Node import Node

class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        newNode = Node(item)
        newNode.setNext(self.head)
        self.head = newNode

    def size(self):
        curr = self.head
        count = 0
        while curr:
            count += 1
            curr = curr.getNext()
        return count

    def search(self, item):
        curr = self.head
        while curr:
            if curr.getData() == item:
                return True
            curr = curr.getNext()
        return False

    def remove(self, item):
        curr = self.head
        prev = None
        while curr:
            if curr.getData() == item:
                if not prev:
                    self.head = curr.getNext()
                    break;
                else:
                    prev.setNext(curr.getNext())
                    break;
            prev = curr
            curr = curr.getNext()

    def append(self,item):
        curr = head
        while curr.getNext():
            curr = curr.getNext()
        curr.setNext(Node(item))

    def index(self, item):
        curr = self.head
        index = 0
        while curr:
            if curr.getData() == item:
                return index
            curr = curr.getNext()

    def insert(self, pos, item):
        current = self.head
        for i in range(pos):
            current = current.getNext()
        newNode = Node(item)
        newNode.setNext(current.getNext())
        current.setNext(newNode)

    def pop(self, index):
        self.remove(self.getItem(index))

if __name__ == '__main__':
    mylist = UnorderedList()

    mylist.add(31)
    mylist.add(77)
    mylist.add(17)
    mylist.add(93)
    mylist.add(26)
    mylist.add(54)

    print(mylist.size())
    print(mylist.search(93))
    print(mylist.search(100))

    mylist.add(100)
    print(mylist.search(100))
    print(mylist.size())

    mylist.remove(54)
    print(mylist.size())
    mylist.remove(93)
    print(mylist.size())
    mylist.remove(31)
    print(mylist.size())
    print(mylist.search(93))