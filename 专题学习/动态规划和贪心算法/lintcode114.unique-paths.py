class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        dp = [[0 for j in range(m)] for i in range(n)]
        
        for j in range(m):
            dp[0][j] = 1 
        for i in range(n):
            dp[i][0] = 1 
        
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
        return dp[n-1][m-1]