class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            return

        node.prev = self.head
        self.head = node

    def pop(self):
        if self.head is None:
            return None

        head = self.head
        self.head = self.head.prev
        return head.data

    def peek(self):
        if self.head is None:
            return None
        return self.head.data

# TEST...
stk = Stack()

print(stk.peek())

stk.push(42)
stk.push(-42)

print(stk.peek())

print(stk.pop())
print(stk.pop())
print(stk.pop())
# stk.push(-42)
# stk.push(-0.42)

# print(stk.pop())
# print(stk.pop())
# print(stk.pop())

# print(stk.peek())
# stk.pop()

# print(stk.peek())
# stk.pop()

# print(stk.peek())
# ...TEST

# while stk.head is not None:
#     print(stk.pop())
