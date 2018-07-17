from Node import Node

class OrderedList:

    def __init__(self):
        self.head = None

    def add(self, item):
        curr = self.head
        prev = None
        temp = Node(item)
        if curr is None:
            temp.setNext(self.head)
            self.head = temp
        while(curr):
            if curr.getData() > item:
                prev.setNext(temp)
                temp.setNext(curr)
                break;
            curr = curr.getNext()
            prev = prev.getNext()

    def search(self, item):
        curr = self.head
        while curr:
            if curr.data == item:
                return True
            curr = curr.getNext()


    def size(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.getNext()
        return curr

    def isEmpty(self):
        return self.size() == 0

def print(orderedList):
    node = orderedList.head
    print(node.getData())
    while node:
        print(node.getData())
        node = node.getNext()

if __name__ == '__main__':
    ol = OrderedList()
    ol.add(2)
    print(ol)