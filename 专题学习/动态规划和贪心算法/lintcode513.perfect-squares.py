'''
Given a positive integer n, find the least number of perfect square numbers
 (for example, 1, 4, 9, 16, ...) which sum to n.

Example
Example 1:

Input: 12
Output: 3
Explanation: 4 + 4 + 4
Example 2:

Input: 13
Output: 2
Explanation: 4 + 9
'''
class Solution:
    """
    @param n: a positive integer
    @return: An integer
    """
    def numSquares(self, n):
        
        if n == 1:
            return 1

        dp = [i for i in range(n + 1)]
        num_squares = [i ** 2 for i in range(1, n//2 + 1)]
        # print(num_squares)
        index_squares = 0

        for i in range(1, n + 1):
            if i in num_squares:
                dp[i] = 1
                index_squares += 1
            else:
                for j in range(index_squares):
                    dp[i] = min(dp[i], dp[i - num_squares[j]] + 1)
            # print(dp)
        return dp[n]
