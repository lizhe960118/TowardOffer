#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#
# https://leetcode.com/problems/merge-sorted-array/description/
#
# algorithms
# Easy (35.10%)
# Total Accepted:    340.1K
# Total Submissions: 968.9K
# Testcase Example:  '[1,2,3,0,0,0]\n3\n[2,5,6]\n3'
#
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as
# one sorted array.
# 
# Note:
# 
# 
# The number of elements initialized in nums1 and nums2 are m and n
# respectively.
# You may assume that nums1 has enough space (size that is greater or equal to
# m + n) to hold additional elements from nums2.
# 
# 
# Example:
# 
# 
# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# 
# Output: [1,2,2,3,5,6]
# 
# 
#
class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        a = len(nums1)
        b = len(nums2) 

        # if a != b + n:
        #     return None

        a = a - 1
        b = b - 1
        m = m - 1
        n = n - 1
        while m >= 0 and n >= 0:
            if nums1[m] >= nums2[n]:
                nums1[a] = nums1[m]
                m -= 1
            else:
                nums1[a] = nums2[n]
                n -= 1
            a -= 1
        
        while m >= 0:
            nums1[a] = nums1[m]
            m -= 1
            a -= 1
        
        while n >= 0:
            nums1[a] = nums2[n]
            n -= 1
            a -= 1
        
        # return nums1

# if __name__ == "__main__":
#     print(Solution().merge([1,2,3,0,0,0], 3, [2,5,6],3))