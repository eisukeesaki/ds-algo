class CircularBuffer:
    def __init__(self, capacity: int):
        self.buffer = [None] * capacity
        self.capacity = capacity
        self.head = 0
        self.tail = 0
        self.size = 0

    def enqueue(self, value):
        if self.tail == self.capacity:
            self.head = (self.head + 1) % self.capacity

        self.buffer[self.tail] = value
        self.tail += 1
        self.size += 1

    def __str__(self):
        return str(self.buffer)

cb = CircularBuffer(7)

cb.enqueue(1)  # tail
cb.enqueue(2)
cb.enqueue(3)
cb.enqueue(4)
cb.enqueue(5)
cb.enqueue(6)
cb.enqueue(7)  # head, size
cb.enqueue(8)  # going to be out of range

print(cb)
