class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        cur_index = len(nums) // 2

        count_move = 0
        for i in range(cur_index):
            count_move += nums[cur_index] - nums[i]
        for i in range(cur_index+1, len(nums)):
            count_move += nums[i] - nums[cur_index]

        return count_move