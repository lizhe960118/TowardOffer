# class Solution:
#     def subarraySum(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         sum_each = [None for _ in range(len(nums))]
#         result = 0
#         tmp = []
#         for i in range(len(nums)):
#             if i == 0:
#                 sum_each[i] = nums[i]
#             else:
#                 sum_each[i] = nums[i] + sum_each[i-1]
#         print(sum_each)
#         for each in sum_each:              
#             if each == k:
#                 result += 1
#             for each_tmp in tmp:
#                 if each - each_tmp == k:
#                     result += 1                        
#             tmp.append(each)
#         return result

# class Solution:
#     def subarraySum(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         dp = [[None for _ in range(len(nums))] for _ in range(len(nums))]
#         result = 0
#         # 初始化dp
#         for i in range(len(nums)):
#             if i == 0:
#                 dp[0][i] = nums[i]
#             else:
#                 dp[0][i] = nums[i] + dp[0][i-1]
#         print(dp)       
#         for i in range(1, len(nums)):
#              for j in range(i, len(nums)):
#                 dp[i][j] = dp[0][j] - dp[0][i-1]
#         print(dp)
#         for i in range(len(nums)):
#              for j in range(len(nums)):
#                 if dp[i][j] == k:
#                     result += 1                        
#         return result

class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dp = {0:1}
        sum_tmp = 0
        result = 0
        for num in nums:
        	sum_tmp += num
        	if (sum_tmp - k) in dp:
        		result += dp[sum_tmp - k]
        	if sum_tmp not in dp:
        		dp[sum_tmp] = 1
        	else:
        		dp[sum_tmp] += 1
        return result


if __name__ == '__main__':
	print(Solution().subarraySum([3, 4, 7, 2, -3, 1, 4, 2], 7))