class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

        def set_next(self, node):
            self.next = node

        def __repr__(self):
            return f"Node({self.data})"


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail  = None #using tail to optimize Order for inserting into tail - from O(n) to O(1)

    # currently O(n) - cause have to loop through the linked list to find the tail
    
    def add_to_tail(self, node):
        head = self.head
        if head is None:
            self.head = node
            self.tail = node
            return
        # using tail to optimize adding to tail - O(1)
        tail = self.tail
        tail.set_next(node)
        self.tail = node

        # O(n) - relevant if tail is not used
        # for node in self:
        #     if node.next is None:
        #         node.set_next(node)
        #         return

    def remove_from_front(self):
        if self.head is None:
            return None
        head = self.head
        self.head = head.next
        if self.head is None:
            self.tail = None  # if the list is now empty, set tail to None
        #clean up the removed node pointer
        head.next = None
        return head
    
    # This function is not relevant to making an O(1) queue linkedlist- which is what this tail optimation is for but still
    # pretty useful for adding or deciding where the order of the queue tail------->head or head<----tail but ofcourse
    # you would have to write an O(1) implementation for the tail to head
    def add_to_front(self,node):
        # O(1) operation reagrdless but including tail to carter for prev optimization
        node.set_next(self.head)
        if self.head is None:
            self.tail = node
        self.head = node


    # returns a list of nodes in the linked list
    def __iter__(self):
        head = self.head
        while head is not None:
            yield head
            head = head.next
