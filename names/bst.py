class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
                if not self.left:
                    self.left = BinarySearchTree(value)
                else:
                    self.left.insert(value)

        if value >= self.value:
                if not self.right:
                    self.right = BinarySearchTree(value)
                else:
                    self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #if target == self.value return it
        if target == self.value:
            return True
        # go left or right if smaller or bigger
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)

        if target >= self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)