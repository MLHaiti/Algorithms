# FIFO - first in first output

class Queue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return self.queue == []

    def enQueue(self, data):
        self.queue.append(data)

    def deQueue(self):
        data = self.queue[0]
        del self.queue
        return data

    def peek(self):
        return self.queue[0]

    def sizeQueue(self):
        return len(self.queue)

queue = Queue()
queue.enQueue(20)
queue.enQueue(11)
queue.enQueue(60)
print(queue.sizeQueue())
