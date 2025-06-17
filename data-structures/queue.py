from collections import deque


class Queue:
    def __init__(self):
        self.items = deque()

    # implemenation head<---- ----tail for O(1) time complexity
    # else i would have O(n) complexity for tail---> head and using insert(0, item)
    def enqueue(self, item):
        self.items.append(item)

    # poping from the front of the queue
    def dequeue(self):
        if len(self.items) == 0:
            return None
        return self.items.popleft()

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[0]
