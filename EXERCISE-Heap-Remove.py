class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)


    def _sink_down(self, index):
        #setting max index . the value present in the root
        max_index = index
        while True:
            #calculate the left and right index by calling the helper methods
            left_index = self._left_child(index)
            right_index = self._right_child(index)
            # check if there is a value in the left index and if the value in the left index is greater than the max_index(value)of the root then left becomes max_index
            if (left_index < len(self.heap) and 
                    self.heap[left_index] > self.heap[max_index]):
                max_index = left_index
            #check if there is a value in the right index and if the value pointed by the right index is greater than the max_index(value)  of the root then right becomes max_index
            if (right_index < len(self.heap) and 
                    self.heap[right_index] > self.heap[max_index]):
                max_index = right_index

            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return
    def remove(self):
        #while heap is empty
        if len(self.heap)==0:
            return None
        #while 1 item in the heap
        if len(self.heap)==1:
            return self.heap.pop()
        #when two or more items.Set a pointer and save as a variable the value in position[0]
        max_value =self.heap[0]
        #move the value popped to the root
        self.heap[0]=self.heap.pop()
        #sink down
        self._sink_down(0)
        #return the value that was popped
        return max_value                   
    ## WRITE REMOVE METHOD HERE ##
    #                            #
    #                            #
    #                            #
    #                            #
    ##############################



myheap = MaxHeap()
myheap.insert(95)
myheap.insert(75)
myheap.insert(80)
myheap.insert(55)
myheap.insert(60)
myheap.insert(50)
myheap.insert(65)

print(myheap.heap)


myheap.remove()

print(myheap.heap)


myheap.remove()

print(myheap.heap)


"""
    EXPECTED OUTPUT:
    ----------------
    [95, 75, 80, 55, 60, 50, 65]
    [80, 75, 65, 55, 60, 50]
    [75, 60, 65, 55, 50]

"""

