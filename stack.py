class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
            return self.head
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is not None:
            popped = self.head.data
            self.head = self.head.next
            print(popped)