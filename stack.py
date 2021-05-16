import LinkedLists
from LinkedLists import LinkedList

class Stack(LinkedList):
    def __init__(self):
        self.head = None

    def insert(self, data):
        self.head = self.add_in_the_end(data)
        self.print_()

    def pop(self):
        if self.head is not None:
            if self.head.next:
                print(self.head.next.data)
                self.head.next = None
                return
            if self.head.data:
                print(self.head.data)
                self.head = None
                return