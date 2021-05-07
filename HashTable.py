class HashTable:
    def __init__(self):
        self.SIZE = 100
        self.array = [None for i in range(self.SIZE)]

    def hash_function(self, key):
        hash_num = 0
        for char in key:
            hash_num += ord(char)
        mode = hash_num % self.SIZE
        return mode

    def add(self, key, value):
        index = self.hash_function(key)
        self.array[index] = value

    def sort(self, key):
        index = self.hash_function(key)
        return self.array[index]


def test_add_and_sort():
    h = HashTable()
    h.add("september", 2010)
    value = h.sort("september")
    print(value)


if __name__ == '__main__':
    test_add_and_sort()