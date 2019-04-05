'''
Input: [4,2,4,5,3,7]
	Output:  4
	
	Explanation: 
	LIS is [2,4,5,7]
'''

class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        if nums is None or len(nums) == 0:
            return 0
            
        n = len(nums)

        # dp[i]表示第i个位置LIS的长度
        dp = [1 for i in range(n)]

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        # print(dp)
        return max(dp)

    # 优化：dp + 二分查找
    def longestIncreasingSubsequence_ii(self, nums):
        if nums is None or len(nums) == 0:
            return 0 
        
        n = len(nums)

        B = []
        B.append(nums[0])

        for i in range(1, n):
            if nums[i] > B[-1]:
                B.append(nums[i])
            else:
                index = self.find_index(B, nums[i], 0, len(B) - 1)
                print(B)
                B[index] = nums[i]

        return len(B)

    def find_index(self, nums, num, start, end):
        while start + 1 < end:
            mid =  (start + end) // 2 # important！
            if nums[mid] == num:
                return mid 
            elif nums[mid] < num:
                start = mid + 1
            else:
                end = mid 
        
        if nums[start] >= num:
            return start 

        if nums[end] >= num:
            return end

if __name__ == "__main__":
    print(Solution().longestIncreasingSubsequence_ii([88,4,24,82,86,1,56,74,71,9,8,18,26,53,77,87,60,27,69,17,76,23,67,14,98,13,10,83,20,43,39,29,92,31,0,30,90,70,37,59]))    