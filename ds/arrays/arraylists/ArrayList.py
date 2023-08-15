class ArrayList:
    def __init__(self):
        self._cap = 1
        self.size = 0
        self._data = [None] * 1

    def at(self, i):
        if i > self.size - 1 or i < 0:
            raise IndexError("index out of bounds")

        return self._data[i]

    def resize(self, cap):
        resized = [None] * cap
        for i in range(self.size):
            resized[i] = self._data[i]

        self._data = resized
        self._cap = cap

    def push(self, data):
        if self.size >= self._cap:
            self.resize(2 * self._cap)

        self._data[self.size] = data
        self.size += 1

    def insert(self, idx, item):
        if idx < 0 or idx >= self.size:
            raise IndexError("index out of bounds")

        if self.size >= self._cap:
            self.resize(2 * self._cap)

        for i in range(self.size, idx, -1):
            self._data[i] = self._data[i-1]
        self._data[idx] = item
        self.size += 1

    def remove(self, idx):
        # TODO: reduce the capacity of the list when the number of elements drops below a certain fraction of the capacity
        if idx < 0 or idx >= self.size:
            raise IndexError("index out of bounds")

        for i in range(idx, self.size - 1):
            self._data[i] = self._data[i+1]
        self._data[self.size - 1] = None

        self.size -= 1

# TEST remove...
print("INSTANTIATE")
al = ArrayList()
print(al._data)

print("PUSH")
al.push(10)
al.push(20)
al.push(30)
al.push(40)
al.push(50)
print(al._data)

print("REMOVE")
al.remove(3)
print(al._data)
# ...TEST remove

# TEST insert...
# print("INSTANTIATE")
# al = ArrayList()
# print(al._data)

# print("PUSH")
# al.push(10)
# al.push(20)
# al.push(30)
# al.push(40)
# al.push(50)
# print(al._data)

# print("INSERT")
# al.insert(4, 0)
# print(al._data)
# ...TEST insert