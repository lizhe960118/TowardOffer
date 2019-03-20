class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor_iter = 0
        for i in range(len(nums)):
            xor_iter ^= nums[i]

        bit_flag = xor_iter & ((~ xor_iter) + 1)

        res = [0, 0]
        for i in range(len(nums)):
            if nums[i] & bit_flag == 0:
                res[0] ^= nums[i]
            else:
                res[1] ^= nums[i]
                
        return res 