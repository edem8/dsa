from collections import deqeue


class Stack:
    def __init__(self):
        self.items = deqeue()

    def push(self, item):
        self.items.append(item)

    # using list however, i would have had to use del keyword to delete the value from the list
    def pop(self):
        if len(self.items) == 0:
            return None
        val = self.items.pop()
        

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)
