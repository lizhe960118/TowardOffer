class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        start = -1
        end = -2
        max_tmp = nums[0]
        min_tmp = nums[n-1]
        
        for i in range(len(nums)):
            max_tmp = max(max_tmp, nums[i])
            min_tmp = min(min_tmp, nums[n-1-i])
            
            if nums[i] < max_tmp:
                end = i
            if nums[n-1-i] > min_tmp:
                start = n-1-i
        
        result = end - start + 1 
        return result