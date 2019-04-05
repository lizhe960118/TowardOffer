class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        n = len(grid)
        m = len(grid[0])

        # dp初始化
        # dp = [[0 for _ in range(m)] for _ in range(n)]
        dp = grid

        for j in range(1, m):
            dp[0][j] += dp[0][j - 1]

        for i in range(1, n):
            dp[i][0] += dp[i - 1][0]

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] += min(dp[i-1][j], dp[i][j-1])

        return dp[n-1][m-1] 
