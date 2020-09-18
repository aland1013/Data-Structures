"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        self.length += 1
        old_head = self.head
        new_head = ListNode(value, None, old_head)
        
        self.head = new_head
                
        if old_head:
            old_head.prev = new_head
        else:
            self.tail = new_head
                 
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.length == 0:
            return None
        else:
            value = self.head.value
            self.length -= 1
            
            if self.length == 0:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            
            return value    
        
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        self.length += 1
        old_tail = self.tail
        new_tail = ListNode(value, self.tail, None)
        
        if self.length == 1:
            self.head = new_tail
            self.tail = new_tail
        else:
            old_tail.next = new_tail
            self.tail = new_tail
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.length == 0:
            return None
        else:
            value = self.tail.value
            self.length -= 1
        
            if self.length == 0:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None
        
            return value
                    
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if self.head == node or self.length == 1:
            return
        else:
            if self.tail == node:
                new_tail = node.prev
                new_tail.next = None
                self.tail = new_tail
            else:
                left = node.prev
                right = node.next
                left.next = right
                right.prev = left
                
            self.head.prev = node
            node.prev = None
            node.next = self.head
            self.head = node
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if self.tail == node or self.length == 1:
            return
        else:
            if self.head == node:
                new_head = node.next
                new_head.prev = None
                self.head = new_head
            else:
                left = node.prev
                right = node.next
                left.next = right
                right.prev = left
            
            self.tail.next = node
            node.next = None
            node.prev = self.tail
            self.tail = node

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.length == 0:
            return
        else:
            self.length -= 1
            
            if self.length == 0:
                self.head = None
                self.tail = None
            elif self.length == 1:
                if self.head == node:
                    self.head = self.tail
                else:
                    self.tail = self.head
            else:
                if self.head == node:
                    self.head = self.head.next
                    self.head.prev = None
                elif self.tail == node:
                    self.tail = self.tail.prev
                    self.tail.next = None
                else:
                    left = node.prev
                    right = node.next
                    left.next = right
                    right.prev = left
                   
    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        current_node = self.head
        values = [current_node.value]
        while current_node.next:
            current_node = current_node.next
            values.append(current_node.value)
        
        return max(values)