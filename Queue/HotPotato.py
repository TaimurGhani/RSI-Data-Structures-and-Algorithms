from Queue import Queue

def hotPotato(namelist, num):
    names = Queue()
    for name in namelist:
        names.enqueue(name)

    while names.size() != 1:
        for i in range(num):
            names.enqueue(names.dequeue())
        names.dequeue()

    return names.dequeue()



if __name__ == '__main__':
    print(hotPotato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))