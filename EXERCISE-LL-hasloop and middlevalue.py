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
     def print_list(self):
         temp=self.head
         while temp is not None:
            print (temp.value)
            temp=temp.next
     def append(self,value):
         new_node = Node(value)
         if self.head is None:
             self.head = new_node
             self.tail = new_node
         else:
             self.tail.next = new_node
             self.tail = new_node
             self.Length+=1
             return True 
         

     def find_middle_node(self):
         fast=self.head
         slow=self.head
         while fast and fast.next is not None:
             slow=slow.next
             fast=fast.next.next
         return slow.value
   
     def has_loop(self):
         fast=self.head
         slow=self.head
         while fast and fast.next is not None:
             slow=slow.next
             fast=fast.next
             if fast==slow:
                 return True
         return False
my_linked_list = LinkedList(5)
my_linked_list.append(4)
my_linked_list.append(3)
my_linked_list.append(2)
my_linked_list.append(1)

my_linked_list.print_list()
print(my_linked_list.has_loop())


print('Middle value', my_linked_list.find_middle_node())



"""
    EXPECTED OUTPUT:
    ----------------
    Head: 4
    Tail: 4
    Length: 1
    
"""

                                                                                                                    