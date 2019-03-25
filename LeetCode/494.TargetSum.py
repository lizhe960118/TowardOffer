class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        n = len(nums)
        sum_all = sum(nums)
        sum_tmp = 0
        dp = [[0 for _ in range(2*sum_all + 1)] for _ in range(n+1)]
        dp[0][sum_all] = 1
        for i, num in enumerate(nums):
        	sum_tmp += num
        	for j in range(sum_all - sum_tmp, sum_all + sum_tmp + 1):
        		if j - num >= 0:
        			dp[i + 1][j] += dp[i][j - num] 
        		if j + num <= 2 * sum_all:
        			dp[i + 1][j] += dp[i][j + num]
        return dp[n][sum_all+S]


class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        n = len(nums)
        sum_all = sum(nums)
        sum_tmp = 0
        dp = [0 for _ in range(2*sum_all + 1)]
        dp[sum_all] = 1
        for i, num in enumerate(nums):
            dp_new = [0 for _ in range(2*sum_all + 1)]
            sum_tmp += num
        	for j in range(sum_all - sum_tmp, sum_all + sum_tmp + 1):
        		if j - num >= 0:
        			dp_new[j] += dp[j - num] 
        		if j + num <= 2 * sum_all:
        			dp_new[j] += dp[j + num]
            dp = dp_new
        return dp[n][sum_all+S]

class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        sum_all = sum(nums)
        if sum_all < S:
            return 0
        self.result = 0
        self.dfs(nums, 0, S)
        return self.result
    
    def dfs(self, nums, d, S):
        if d == len(nums):
            if S == 0:
                self.result += 1
                return 
        if d < len(nums):
            self.dfs(nums, d+1, S + nums[d])
            self.dfs(nums, d+1, S - nums[d])
                