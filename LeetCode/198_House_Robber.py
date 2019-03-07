class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        count_one = 0
        count_two = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                count_two = max(count_two + nums[i], count_one)
            else:
                count_one = max(count_one + nums[i], count_two)
        return max(count_one, count_two)