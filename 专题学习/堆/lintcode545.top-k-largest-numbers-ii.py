import heapq

class Solution:
    """
    @param: k: An integer
    """
    def __init__(self, k):
        self.h = []
        self.k_num = k

    """
    @param: num: Number to be added
    @return: nothing
    """
    def add(self, num):
        if len(self.h) < self.k_num:
            heapq.heappush(self.h, num)
        else:
            smallest = heapq.heappop(self.h)
            if num > smallest:
                heapq.heappush(self.h, num)
            else:
                heapq.heappush(self.h, smallest)

    """
    @return: Top k element
    """
    def topk(self):
        self.h.sort()
        return self.h[::-1]