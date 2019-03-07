class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """

        :param nums1:List[int]
        :param nums2:List[int]
        :return:float
        """
        len1 = len(nums1)
        len2 = len(nums2)
        k = (len1 + len2) // 2  # 除法运算,返回商的整数部分，抛弃余数
        if (len1 + len2) % 2 == 0:
            return (self.findK(nums1, nums2, k) +
                    self.findK(nums1, nums2, k - 1)) / 2.0
        else:
            return self.findK(nums1, nums2, k)

    def findK(self, nums1, nums2, k):
        if not nums1:
            return nums2[k]
        if not nums2:
            return nums1[k]
        if k == 0:
            return min(nums1[0], nums2[0])
        len1 = len(nums1)
        len2 = len(nums2)
        if nums1[len1 // 2] > nums2[len2 // 2]:
            if k > len1 // 2 + len2 // 2:
                return self.findK(
                    nums1, nums2[len2 // 2 + 1:], k - len2 // 2 - 1)
            else:
                return self.findK(nums1[:len1 // 2], nums2, k)
        else:
            if k > len1 // 2 + len2 // 2:
                return self.findK(nums1[len1 // 2 + 1:],
                                  nums2, k - len1 // 2 - 1)
            else:
                return self.findK(nums1, nums2[:len2 // 2], k)


if __name__ == "__main__":
    print(Solution().findMedianSortedArrays([1, 2], [1, 2, 3]))
    print(Solution().findMedianSortedArrays([], [2, 3]))
    print(Solution().findMedianSortedArrays([8], [1,2,3,4]))
    print(Solution().findMedianSortedArrays([1, 2], [3, 4]))
