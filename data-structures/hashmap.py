class HashMap:
    def __init__(self, size):
        self.hashmap = [None] * size

    def key_to_index(self, key):
        # Assuming that our key is a string we could write the algorithm below
        # This is however not SOLID cause "abc" and "bac" will collide and return the same index
        # sum = 0
        # for c in key:
        #     sum += ord(c)
        # return sum % len(self.hashmap)
        return hash(key) % len(self.hashmap)
        # even thpugh this is more robust you can still have collisions
        # hash(val1)-->10 and then % 10 = 0
        # hash(val2)-->20 and then % 10 = 0
        # real world hashmaps handles collision in two ways 1.chaining(each slot in the map hold a list of key value pairs) 2.open addressing(look for the next free slot)


    def insert(self, key, value):
        i = self.key_to_index(key)
        # Hashmap store key and value pairs so at every index of our list we want to store that as tuple
        self.hashmap[i] = (key, value)

    def get(self, key):
        i = self.key_to_index(key)
        tup  = self.hashmap[i]
        if tup is None:
            raise Exception("Key not found")
        # return the value since key is at tup[0]
        return tup[1]