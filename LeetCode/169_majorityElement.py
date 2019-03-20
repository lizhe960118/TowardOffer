# class Solution(object):
#     def majorityElement(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if nums is None:
#             return None

#         self.quickSortHelper(nums, 0, len(nums) - 1)

#         return nums[(len(nums) - 1) // 2]
        
#     def quickSortHelper(self, nums, start, end):
#         if start == end:
#             return 

#         mid = start + (end - start) // 2
#         pivot = nums[mid]

#         left = start
#         right = end
#         while left <= right:
#             while left <= right and nums[left] < pivot:
#                 left += 1
#             while left <= right and nums[right] > pivot: 
#                 right -= 1
#             if left <= right:
#                 nums[left], nums[right] = nums[right], nums[left]
#                 left += 1
#                 right -= 1
#         self.quickSortHelper(nums, start, right)
#         self.quickSortHelper(nums, left, end)

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority_index = 0
        cur_count = 1

        for i in range(len(nums)):
            if nums[majority_index] == nums[i]:
                cur_count += 1
            else:
                cur_count -= 1
            if cur_count == 0:
                majority_index = i 
                cur_count = 1

        return nums[majority_index]
