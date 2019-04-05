import heapq

class Solution:
    """
    @param n: An integer
    @return: return a  integer as description.
    """
    def nthUglyNumber(self, n):
        h = [1]
        visited = set([1])
        
        for i in range(n):
            val = heapq.heappop(h) # 出堆n次即可
            multi_nums = [2, 3, 5]
            for num in multi_nums:
                if val * num not in visited:
                    visited.add(val * num)
                    heapq.heappush(h, val * num)
                    
        return val
        