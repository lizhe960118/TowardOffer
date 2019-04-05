'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.

Example:
A = [2,3,1,1,4], return true.
A = [3,2,1,0,4], return false.
'''

# greedy method
'''
class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        n = len(A)
        
        index = 0
        can_reach = A[0]
        
        while index <= can_reach and index < n:
            can_reach = max(can_reach, index + A[index])
            index += 1 
    
        return can_reach >= n-1
'''

class Solution:
    def canJump(self, A):
        n = len(A)
        if n == 1:
            return True
        dp = [False for i in range(n)]
        if A[0] > 0:
            dp[0] = True
        for i in range(1, n):
            for j in range(i):
                if dp[j] and j + A[j] >= i:
                    dp[i] = True 
        return dp[n-1] 
