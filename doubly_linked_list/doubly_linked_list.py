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
        value = self.head.value
        
        if self.length == 0:
            return value
        
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
            return value
        
        self.length -= 1
        self.head = self.head.next
        
        return value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_tail = ListNode(value, self.tail, None)
        
        if self.length == 0:
            self.length = 1
            self.head = new_tail
            self.tail = new_tail

        else:
            self.length += 1
            old_tail = self.tail
            old_tail.next = new_tail
            self.tail = new_tail
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        value = self.tail.value
        
        if self.length == 0:
            return value
        
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
            return value
        
        self.length -= 1
        self.tail = self.tail.prev
        
        return value
                    
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        prev_node = node.prev
        next_node = node.next
        
        if not prev_node:
            return
        
        if not next_node:
            prev_node.next = None
            self.tail = prev_node
        else:
            prev_node.next = next_node
            next_node.prev = prev_node
        self.add_to_head(node.value)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        prev_node = node.prev
        next_node = node.next
        
        if not next_node:
            return
        
        if prev_node:
            prev_node.next = next_node
            next_node.prev = prev_node
        else:
            next_node.prev = None
            self.head = next_node
                
        self.add_to_tail(node.value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.length == 0:
            return
        
        if self.length == 1:
            self.length = 0
            self.head = None
            self.tail = None
            return
        
        self.length -= 1
          
        left = node.prev
        right = node.next
        
        if not left:
            self.remove_from_head()
            return
        
        if not right:
            self.remove_from_tail()
            return
        
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