class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
    
    def get_value(self):
        """
        Method to get the value of a node
        """
        return self.value
    
    def get_next(self):
        """
        Method to get the node's next node
        """
        return self.next
    
    def set_next(self, new_next):
        """
        Method to update the node's next node
        """
        self.next = new_next
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def add_to_tail(self, value):
        new_node = Node(value)
        
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
    
    def remove_tail(self):
        if self.head is None and self.tail is None:
            return None
        
        if self.head == self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value
        
        value = self.tail.get_value()
        new_tail = self.head
        while new_tail.get_next() != self.tail:
            new_tail = new_tail.get_next()
        self.tail = new_tail
        self.tail.set_next(None)
        return value
    
    def remove_head(self):
        if self.head is None and self.tail is None:
            return None
        
        if self.head == self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value
        
        value = self.head.get_value()
        self.head = self.head.get_next()
        return value
            
