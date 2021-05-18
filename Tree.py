class Tree:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, data):
        child = Tree(data)
        child.parent = self
        self.children.append(child)
        return child

    def get_level(self):
        level = 0
        parent = self.parent
        while parent is not None:
            level += 1
            parent = parent.parent
        return level

    def print_tree(self):
        level = self.get_level()
        tree = ' ' * level * 3 + '|__' + str(self.data)
        print(tree)
        if len(self.children) == 0:
            return
        for child in self.children:
            child.print_tree()

def test_tree():
    samsung = Tree("samsung")
    phone = samsung.add_child("phones")
    tv = samsung.add_child("tv")
    phone.add_child("galaxy S8")
    phone.add_child("galaxy S9")
    phone.add_child("galaxy S9+")
    tv.add_child("400*600")
    tv.add_child("400*800")
    tv_child = tv.add_child("400*300")
    samsung.print_tree()


if __name__ == "__main__":
    test_tree()