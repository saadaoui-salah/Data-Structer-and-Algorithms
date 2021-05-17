class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

class Qeue:
    def __init__(self):
        self.head = None

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
            return self.head
        new_node = Node(data)
        self.head.next = new_node
        self.head = self.head.next

    def pop(self):
        if self.head is not None:
            popped = self.head.data
            self.head = self.head.next
            return popped