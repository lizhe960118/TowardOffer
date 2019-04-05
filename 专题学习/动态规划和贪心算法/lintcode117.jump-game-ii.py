'''
Example:
Given array A = [2,3,1,1,4]
The minimum number of jumps to reach the last index is 2. 
(Jump 1 step from index 0 to 1, then 3 steps to the last index.)
'''

'''
class Solution:
    def jump(self, A):
        n = len(A)

        dp = [i for i in range(n)]

        for i in range(1, n):
            for j in range(i):
                if j + A[j] >= i:
                    dp[i] = min(dp[i], dp[j] + 1) 

        return dp[n-1] 
'''

'''
class Solution:
    def jump(self, A):
        n = len(A)
        if n == 1:
            return 0

        step = [i for i in range(n)]
        can_reach = A[0]
        if can_reach >= n-1:
            return 1
        
        for i in range(1, can_reach + 1):
            step[i] = 1

        for i in range(1, n):
            for j in range(i, can_reach + 1):
                if j + A[j] >= n - 1:
                    return step[j] + 1 
                if j + A[j] > can_reach:
                    for k in range(can_reach+1, j + A[j] + 1):
                        step[k] = min(step[j]+1, step[k])
                    can_reach = j + A[j]
                # print(step)

        return step[n-1]
'''

class Solution:
    """
    @param A: A list of integers
    @return: An integer
    """
    def jump(self, A):
        n = len(A)
        if n == 1:
            return 0
            
        index = 0
        can_reach = 0
        step = 0
        
        while index <= can_reach and index < n:
            if index + A[index] > can_reach:
                can_reach = index + A[index]
                step += 1
            if can_reach >= n - 1:
                return step
            index += 1 
    
        return -1 