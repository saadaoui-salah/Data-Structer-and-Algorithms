import LinkedLists

class Stack:
    def __init__(self):
        self.block = LinkedList()

    def insert(self, data):
        self.block.add_in_the_end(data)

    def pop(self):
        print(self.block.data)
        self.block.data = None


    