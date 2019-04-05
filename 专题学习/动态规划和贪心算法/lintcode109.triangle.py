class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, triangle):
        A = triangle
        n = len(A)
        
        for i in range(1, n):
            for j in range(len(A[i])):
                if j == 0:
                    A[i][0] += A[i-1][0]
                elif j == len(A[i]) - 1:
                    A[i][j] += A[i-1][len(A[i]) - 2]
                else:
                    A[i][j] = min(A[i-1][j - 1] + A[i][j], A[i-1][j] + A[i][j])
        # print(A)
        return min(A[n-1])