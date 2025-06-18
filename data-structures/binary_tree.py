class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        # insert value into the node's vlaue if its empty
        # if not we have to check if the value is equal to its value, lesser or greater
        # create left or right BSTnodes (recursive calls) and then insert the value accordingly
        if self.val is None:
            self.val = val
            return
        if self.val == val:
            return
        # if val is less than the node's value, we insert it into the left child
        # if theres  no left child, we create a new BSTNode for the left child
        # if theres is a left child then we have to INSERT the value into the left child by making all these check again hence the recursive call
        if self.val > val:
            if self.left is None:
                self.left = BSTNode(val)
            self.left.insert(val)
            return
        
        # if val is greater than the node's value, we insert it into the right child
        # if theres  no right child, we create a new BSTNode for the right child
        # if theres is a right child then we have to INSERT the value into the right child by making all these check again hence the recursive call
        if self.right is None:
            self.right = BSTNode(val)
        self.right.insert(val)
        return
