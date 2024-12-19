class ListNode:
    """
    A node in a singly-linked list.
    """
    def __init__(self, data=None, next=None):
        self.data= data
        self.next= next
    
class SinglyLinkedList:
    def __init__(self):
        """
        Create a new singly-linked list.
        Takes O(1) time.
        """
        self.head = None
        if self.head is None:
            self.curr_node = ListNode()

        self.curr_node= self.head


    def append(self, data):
        """
        Insert a new element at the end of the list.
        Takes O(n) time.
        """
        new_node= ListNode(data)
        if self.head is None:
            self.head = new_node
            return
        end= self.head
        while (end.next):
            end = end.next
        end.next = new_node


        
    def find(self, key):
        """
        Search for the first element with `data` matching
        `key`. Return the element or `None` if not found.
        Takes O(n) time.
        """
        node= self.head
        while (node.data != key):
            node= node.next
        return node
        
    def remove(self, key):
        """
        Remove the first occurrence of `key` in the list.
        Takes O(n) time.
        """
        curr_node = self.head
        if curr_node is not None:
            if curr_node.data == key:
                self.head = curr_node.next
                curr_node = None
            return
        while (curr_node is not None):
            if curr_node.data == key:
                break
            prev_node= curr_node
            if curr_node.next is not None:
                curr_node = curr_node.next
            else: 
                return
        prev_node.next = curr_node.next
        curr_node= None

        
        

