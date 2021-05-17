class Node:
    def __init__(self, prev, data, next):
        self.next = next
        self.data = data

class Queue:
    def __init__(self):
        self.first = self.last = None

    def en_queue(self, data):
        self.head = Node(data, self.head)
        

    def de_queue(self):
        if self.head is not None:
            popped = self.head.data
            self.head = self.head.next
            return popped



if __name__ == '__main__':
    q = Qeue()
    q.push(1)
    q.push(2)
    q.push(3)
    q.push(4)
    q.push(5)
    popped = q.pop()
    print(popped)
    popped = q.pop()
    print(popped)
    popped = q.pop()
    print(popped)