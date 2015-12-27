class BST:
    "a binary search tree with values for stored keys"
    def __init__(self):
        self.tree = EmptyTreeNode()

    def lookup(self, key):
        return self.tree.lookup(key)

    def insert(self, key, val):
        self.tree = self.tree.insert(key, val)

    def __repr__(self):
        return repr(self.tree)

class EmptyTreeNode:
    def lookup(self, key): # fail at the bottom
        return None

    def insert(self, key, val): # add node at bottom
        return BinaryTreeNode(self, key, val, self)

    def __repr__(self):
        return '*'

class BinaryTreeNode:
    def __init__(self, left, key, val, right):
        self.key, self.val = key, val;
        self.left, self.right = left, right;

    def lookup(self, key):
        if self.key == key:
            return self.val
        elif self.key > key:
            return self.left.lookup(key)
        else:
            return self.right.lookup(key)

    def insert(self, key, val):
        if self.key == key:
            self.val = val
        elif self.key > key:
            self.left = self.left.insert(key, val)
        else:
            self.right = self.right.insert(key, val)
        return self

    def __repr__(self):
        return ('( %s, %s=%s, %s )' %
                (repr(self.left), repr(self.key), repr(self.val), repr(self.right)))

def testBST():
    tree = BST()
    for (key, val) in [('bbb', 1), ('aaa', 2), ('ccc', 3)]:
        tree.insert(key, val)

    print(tree)
    print(tree.lookup('aaa'), tree.lookup('ccc'))
    tree.insert('ddd', 4)
    tree.insert('aaa', 5)
    print(tree)
