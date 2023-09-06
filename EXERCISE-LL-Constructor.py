class Node:
     def __init__(self,value):
        self.value = value
        self.next = None
         
class LinkedList:
     def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.Length = 1
    
my_linked_list = LinkedList(3)

print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.Length)




"""
    EXPECTED OUTPUT:
    ----------------
    Head: 4
    Tail: 4
    Length: 1
    
"""

                                                                                                                    