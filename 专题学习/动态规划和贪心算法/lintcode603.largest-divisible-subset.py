class Solution:
    """
    @param: nums: a set of distinct positive integers
    @return: the largest subset 
    """
    def largestDivisibleSubset(self, nums):
        n = len(nums)
        if n <= 1:
            return nums
        
        result = []
        nums.sort()
        
        dp = [0 for i in range(n)] # dp记录当前位置的最大连续可除序列长度
        record_dict = {} # record_dict记录当前位置对应的前一个最大除数
                
        dp[0] = 1 
        record_dict[nums[0]] = -1
        
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 >= dp[i]:
                        dp[i] = dp[j] + 1
                        record_dict[nums[i]] = nums[j]
        # print(dp)      
        max_index = dp.index(max(dp))
        
        get_value = nums[max_index]
        
        while get_value != -1:
            result.append(get_value)
            get_value = record_dict[get_value]
            
        return result
