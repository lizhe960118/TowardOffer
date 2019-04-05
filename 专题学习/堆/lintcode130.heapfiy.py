class Heapify(object):
    def __init__(self, A=[]):
        self.heap = A
        self.modify()
        
    def siftdown(self, index):
        while(index < len(self.heap)):
            smallest = index
            if (2 * index + 1) < len(self.heap) and self.heap[2 * index + 1] < self.heap[smallest]:
                smallest = 2 * index + 1
            if (2 * index + 2) < len(self.heap) and self.heap[2 * index + 2] < self.heap[smallest]:
                smallest = 2 * index + 2
            if smallest == index:
                break
            self.heap[index], self.heap[smallest] =  self.heap[smallest], self.heap[index]
            index = smallest
        
    def modify(self):
        for i in range(len(self.heap) // 2, -1, -1):
            self.siftdown(i)
        
    def push(self, element):
        self.heap.append(element)
        self.modify()
    
    def pop(self):
        self.heap.pop(0)
        self.modify()
    
    def top(self):
        return self.heap[0]

class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """
    def heapify(self, A):
        heapify_A = Heapify(A)
        A = heapify_A.heap
        
