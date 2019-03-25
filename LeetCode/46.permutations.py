class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        current = []
        self.get_permute(current, nums, result)
        return result

    def get_permute(self, current, nums, result):
        if not nums:
            result.append(current + [])
            return
        for i, v in enumerate(nums):
            current.append(nums[i])
            self.get_permute(current, nums[: i] + nums[i + 1:], result)
            current.pop()


if __name__ == "__main__":
    print(Solution().permute([1, 2, 3]) == [[1, 2, 3], [
          1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])
