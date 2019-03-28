class Node(object):
    def __init__(self, data):
        self.data = data
        self.nextNode = None

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def _size(self):
        return self.size

    def insertStart(self, data):
        newNode = Node(data)
        self.size += 1
        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

    def insertEnd(self, data):
        newNode = Node(data)
        self.size += 1

        actualNode = self.head

        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode

        actualNode.nextNode = newNode

    def remove(self, data):
        currentNode = self.head
        previousNode = None

        while currentNode.data != data:
            previousNode = currentNode
            currentNode = currentNode.nextNode

        if previousNode is None:
            self.head = currentNode.nextNode
            currentNode.nextNode = None
            self.size -= 1
        elif currentNode.data == data:
            previousNode.nextNode = currentNode.nextNode
            currentNode.nextNode = None
            self.size -= 1

    def traverseList(self):
        actualNode = self.head
        while actualNode is not None:
            print("{}".format(actualNode.data))
            actualNode = actualNode.nextNode
