class Node:
    def __init__(self, data, next, prev):
        self.data = data
        self.next = next
        self.prev = prev

class CircularQueue:
    def __init__(self, cap: int):
        self.cap = cap
        self.left = Node(None, None, None)
        self.right = Node(None, None, self.left)
        self.left.next = self.right
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        new = Node(value, self.right, self.right.prev)

        self.right.prev.next = new
        self.right.prev = new
        self.cap -= 1

        return True
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.left.next = self.left.next.next
        self.left.next.prev = self.left

        self.cap += 1

        return True
    def Front(self) -> int:
        if self.isEmpty():
            return -1

        return self.left.next.data
    def Rear(self) -> int:
        if self.isEmpty():
            return -1

        return self.right.prev.data
    def isEmpty(self) -> bool:
        return self.left.next == self.right
    def isFull(self) -> bool:
        return self.cap == 0
        
cap = 5
cq = CircularQueue(cap)
cq.enQueue(42)
cq.enQueue(420)
cq.enQueue(120)
cq.deQueue()
print(cq.Front())
