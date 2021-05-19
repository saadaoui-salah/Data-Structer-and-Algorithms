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