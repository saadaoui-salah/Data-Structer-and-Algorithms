class BSTNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def add_node(self, data):
        if self.data == data:
            return
        if self.data > data:
            if self.right is None:
                self.right = BSTNode(data)
            else:
                self.right.add_node(data)
        else:
            if self.left is None:
                self.left = BSTNode(data)
            else:
                self.left.add_node(data)

    def in_order(self):
        elements = []
        if self.right:
            elements +=self.right.in_order()

        elements.append(self.data)

        if self.left:
            elements += self.left.in_order()
        
        return elements

    def search(self, data):
        if self.data == data:
            return True
        if self.data < data:
            if self.left:
                return self.left.search(data)
            return False
        if self.right:
            return self.right.search(data)
        return False
   
    def get_min(self):
        while self.left:
            self.left = self.left.left
        return self.data
   
    def get_max(self):
        while self.right:
            self.right = self.right.right
        return self.data

def emplement_tree(arr):
    node = BSTNode(arr[0])
    for i in range(1,len(arr)):
        node.add_node(arr[i])
    return node

if __name__ == "__main__":
    elements = [7,12,14,15,27,20,88,23]
    tree = emplement_tree(elements)
    print(tree.in_order())
    print(tree.search(15))
    print(tree.search(22))
    print("min :",tree.get_min())
    print("max :",tree.get_max())
