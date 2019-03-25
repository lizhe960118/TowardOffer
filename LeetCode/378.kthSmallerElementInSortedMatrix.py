import heapq

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        m = len(matrix[0])

        h = []
        for i in range(n):
            for j in range(m):
                heapq.heappush(h, matrix[i][j])

        for i in range(k-1):
            heapq.heappop(h)

        return heapq.heappop(h)

if __name__ == '__main__':
    print(Solution().kthSmallest([[1, 2, 3], [3, 4, 5], [7, 8, 9]], 8))