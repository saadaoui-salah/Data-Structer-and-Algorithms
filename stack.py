class StackNode:
    def __init__(self, data, next):
        self.data = data
        self.next = next
        
class Stack:
    def __init__(self, data):
        self.head = None
        