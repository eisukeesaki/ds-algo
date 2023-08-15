class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def enqueue(self, data):
        new_node = Node(data)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
    def dequeue(self):
        if not self.head:
            return None

        head = self.head
        self.head = self.head.next
        head.next = None
        self.length -= 1

        return head.data
    def peek(self):
        return self.head

# q = Queue()
# q.enqueue(42)
# q.enqueue(-42)
# q.enqueue(420)
# q.dequeue()
# q.dequeue()
# q.dequeue()
# print(q.peek().data)
# q.dequeue()
# print(q.head.next.next.data)