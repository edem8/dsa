class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def min_value(self):
        temp = self
        while temp.left is not None:
            temp = temp.left
        return temp.val

    def max_value(self):
        temp = self
        while temp.right is not None:
            temp = temp.right
        return temp.val

    def delete(self, val):
        # if self doesnt have a value then it doesnt have children nodes so there's nothing to delete in self or down the branch
        if self.val is None:
            return None
        
        # if self has a left child  and the val is less than self's value perform the delete operation on the left child
        if self.val > val:
            if self.left:
                self.left = self.left.delete(val)
            return self

        # if self has a  right children and val is greater than self's value perform the delete operation on the right child
        if self.val < val:
            if self.right:
                self.right = self.right.delete(val)
            return self

        # If the value is same as self's value then we want to delete self

        # if self has no right child return the left child
        if self.right is None:
            return self.left
        # if self has no left child return the right child
        if self.left is None:
            return self.right
        

        # Getting here means they have both children so what we want 
        # to get the min value at the larger child(right child) to be the new node decider and delete that node 
        min_larger_value = self.right
        while min_larger_value.left:
            min_larger_value = min_larger_value.left
        self.val = min_larger_value.val

        # deleting that min_larger value node so it doesnt exist no more
        self.right = self.delete(min_larger_value.val)
        return self
    
    
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
