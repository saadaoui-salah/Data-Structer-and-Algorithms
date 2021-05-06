class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_in_the_beginig(self, data):
        node = Node(data, self.head)
        self.head = node 

    def print_(self):
        if self.head is None:
            print("Linked List is Empty")
            return
        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data) + "----->"
            itr = itr.next
        print(llstr)

linked_list = LinkedList()
linked_list.add_in_the_beginig(0)
linked_list.add_in_the_beginig(1)
linked_list.add_in_the_beginig(2)
linked_list.add_in_the_beginig(3)
linked_list.add_in_the_beginig(4)
linked_list.add_in_the_beginig(5)
linked_list.add_in_the_beginig(6)
linked_list.print_()