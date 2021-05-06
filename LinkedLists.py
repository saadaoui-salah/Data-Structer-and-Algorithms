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

    def add_in_the_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def add_values(self, data_list):
        for data in data_list:
            self.add_in_the_end(data)

    def length(self):
        if self.head is None:
            return 0
        count = 0
        itr = self.head
        while itr.next:
            itr = itr.next
            count += 1
        return count

linked_list = LinkedList()

def test_add_in_the_begning():
    linked_list.add_in_the_beginig(0)
    linked_list.add_in_the_beginig(1)
    linked_list.add_in_the_beginig(2)
    linked_list.add_in_the_beginig(3)
    linked_list.print_()

def test_add_in_the_end():
    linked_list.add_in_the_end(0)
    linked_list.add_in_the_end(1)
    linked_list.add_in_the_end(2)
    linked_list.add_in_the_end(3)
    linked_list.print_()

def test_add_values_and_length():
    linked_list.add_values([0,1,2,3,4,5,6])
    linked_list.print_()
    length = linked_list.length()
    print(length)


test_add_values_and_length()