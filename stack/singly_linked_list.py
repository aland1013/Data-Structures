class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    def add_to_tail(self, value):
        new_node = Node(value)
        self.length += 1
        
        if self.length == 1:
            self.head = new_node
            self.tail = new_node
        
        else:        
            old_tail = self.tail
            old_tail.next = new_node
            self.tail = new_node
    
    def remove_head(self):
        if self.length == 0:
            return None
        
        elif self.length == 1:
            self.length -=1
            value = self.head.value
            self.head = None
            self.tail = None
            return value
    
        else:
            self.length -= 1
            old_head = self.head
            self.head = old_head.next
            return old_head.value
    
    def remove_tail(self):
        if self.length == 0:
            return None
        
        elif self.length == 1:
            self.length -= 1
            value = self.tail.value
            self.head = None
            self.tail = None
            return value
        
        else:
            self.length -= 1
            old_tail = self.tail
            new_tail = self.head
            while new_tail.next != old_tail:
                new_tail = new_tail.next
            self.tail = new_tail
            return old_tail.value
            