class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum_all = sum(nums)
        if sum_all % 2:
        	return False
        dp = [0 for i in range(sum_all + 1)]
        dp[0] = 1
        for num in nums:
        	for i in range(sum_all + 1, -1, -1):
        		if dp[i]:
        			dp[i + num] = 1
        	if dp[sum_all // 2] == 1:
        		return True
       	return False