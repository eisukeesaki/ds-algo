class Node:
    def __init__(self, name):
        self.name = name
        self.children = {}

    def add_dir(self, name):
        new_dir = Node(name)
        self.children[name] = new_dir

root = Node("/")

root.add_dir("home")

print(root.children.keys())
