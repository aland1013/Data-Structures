"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None # left sub-tree
        self.right = None # right sub-tree

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)
            

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        else:
            if target < self.value and self.left:
                return self.left.contains(target)
            elif target > self.value and self.right:
                return self.right.contains(target)
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value    

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        
        if self.left:
            self.left.for_each(fn)
        
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------
    
    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self.left:
            self.left.in_order_print()
        
        print(self.value)
        
        if self.right:
            self.right.in_order_print()
             
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        q = Queue()
        q.enqueue(self)
        
        while len(q) != 0:
            n = q.dequeue()
            
            if n.left:
                q.enqueue(n.left)
            
            if n.right:
                q.enqueue(n.right)
            
            print(n.value)
            
    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        s = Stack()
        s.push(self)
        
        while len(s) != 0:
            n = s.pop()
            
            if n.right:
                s.push(n.right)
            
            if n.left:
                s.push(n.left)
            
            print(n.value)    

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        print(self.value)
        
        if self.left:
            self.left.pre_order_dft()
                
        if self.right:
            self.right.pre_order_dft()

    # Print Post-order recursive DFT
    def post_order_dft(self):
        if self.left:
            self.left.post_order_dft()
        
        if self.right:
            self.right.post_order_dft()
        
        print(self.value)

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        self.storage.append(value)
        return self.storage

    def pop(self):
        if self.size == 0:
            return
        self.size -= 1
        value = self.storage.pop()
        return value

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        self.storage.append(value)

    def dequeue(self):
        if len(self.storage) > 0:
            return self.storage.pop(0)
        
        return None

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_print()
print("post order")
bst.post_order_dft()  
