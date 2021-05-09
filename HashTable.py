class HashTable:
    def __init__(self):
        self.SIZE = 100
        self.array = [[] for i in range(self.SIZE)]

    def hash_function(self, key):
        hash_num = 0
        for char in key:
            hash_num += ord(char)
        mode = hash_num % self.SIZE
        return mode

    def add(self, key, value):
        index = self.hash_function(key)
        found = False
        for i, element in enumerate(self.array):
            if len(element) == 2 and element[0] == key:
                self.array[index][i].append((key, value))
                break
        if not found:
            self.array[index].append((key,value))

    def sort(self, key):
        index = self.hash_function(key)
        if len(self.array[index]) > 0 :
            for element in self.array[index]:
                if element[0] == key:
                    return element[1]
        raise "Key Not Found"

    def delete(self, key):
        index = self.hash_function(key)
        if self.array[index] == None:
            raise "Key Not Found"
            return
        self.array[index] = None
        return True


def test():
    h = HashTable()
    key = "september"
    value = 2010
    h.add(key, value)
    test_value = h.sort("september")
    test_add = test_value == value
    print(test_add)
    deleted = h.delete(key)
    print(deleted)

def test2():
    h = HashTable()
    h.add("march 6", 200)
    h.add("march 17", 400)
    value1 = h.sort("march 6")
    value2 = h.sort("march 17")
    print(value1, value2)
if __name__ == '__main__':
    test()
    test2()