class CircularBuffer:
    def __init__(self, capacity: int):
        self.buffer = [None] * capacity
        self.capacity = capacity
        self.head = 0
        self.tail = 0
        self.size = 0

    def enqueue(self, value):
        if self.size == self.capacity:
            self.head = (self.head + 1) % self.capacity

        self.buffer[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise Exception("Buffer is empty")

        value = self.buffer[self.head]
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return value

    def __str__(self):
        return str(self.buffer)

if __name__ == "__main__":
    cb = CircularBuffer(3)  # capacity is 3
    cb.enqueue(1)
    cb.enqueue(2)
    cb.enqueue(3)
    print(cb)  # [1, 2, 3]
    cb.enqueue(4)  # This will overwrite 1, as the buffer is full
    print(cb)  # [4, 2, 3]
    print(cb.dequeue())  # 2
    print(cb.dequeue())  # 3
    print(cb)  # [4, None, None]
