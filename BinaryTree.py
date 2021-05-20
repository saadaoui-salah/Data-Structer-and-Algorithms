class BSTNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def add_node(self, data):
        if self.data == data:
            return
        if self.data < data:
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
        if self.left:
            elements +=self.left.in_order()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order()
        
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
        if self.left is not None:
            return self.left.get_min()
        return self.data

   
    def get_max(self):
        if self.right is not None:
            return self.right.get_max()
        return self.data

    def calculate_sum(self):
        is_right = self.right is not None 
        is_left = self.left is not None 
        if is_right and is_left :
            return self.right.calculate_sum() + self.left.calculate_sum() + self.data
        if is_right:
            return self.data + self.right.calculate_sum()
        if is_left:
            return self.data + self.left.calculate_sum()
        return self.data
        
def emplement_tree(arr):
    node = BSTNode(arr[0])
    for i in range(1,len(arr)):
        node.add_node(arr[i])
    return node


if __name__ == "__main__":
    elements = [12,7,14,15,10,102,27,20,88,23]
    tree = emplement_tree(elements)
    #print(tree.in_order())
    #print(tree.search(15))
    #print(tree.search(22))
    a = 0
    for i in elements:
        a += i
    print("a",a)
    print("min :",tree.get_min())
    print("max :",tree.get_max())
    print("sum :",tree.calculate_sum())
