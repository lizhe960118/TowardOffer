"""
You have a number of envelopes with widths and heights given as a pair of integers (w, h). 
One envelope can fit into another if and only if both the width and height of
 one envelope is greater than the width and height of the other envelope.
What is the maximum number of envelopes can you Russian doll? (put one inside other)

Example
Given envelopes = [[5,4],[6,4],[6,7],[2,3]],
the maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
"""
class Solution:
    """
    @param: envelopes: a number of envelopes with widths and heights
    @return: the maximum number of envelopes
    """
    def maxEnvelopes(self, envelopes):
        if len(envelopes) <= 1:
            return len(envelopes)
        
        n = len(envelopes)

        envelopes = sorted(envelopes, key=lambda x:x[0])
        # print(envelopes)

        dp = [1 for i in range(n)]
        # dp[0] = 1

        for i in range(1, n):
            for j in range(i):
                if envelopes[i][1] > envelopes[j][1] and envelopes[i][0] > envelopes[j][0]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

    """ bad method
    def maxEnvelopes(self, envelopes):
        if len(envelopes) <= 1:
            return len(envelopes)
        
        n = len(envelopes)

        envelopes = sorted(envelopes, key=lambda x:(x[0],-x[1]))
        # print(envelopes) 这里相当于求最长上升子序列
        
        # dp + 二分查找
        B = [] # 使用B[i]来记录能套i+1个套娃时最近的那个套娃
        B.append(envelopes[0])
        for i in range(1, n):
            if envelopes[i][1] > B[-1][1] and envelopes[i][0] > B[-1][0]:
                B.append(envelopes[i])
            else:
                print(B) 
                index = self.find_index(B, envelopes[i], 0, len(B) - 1)
                B[index] = envelopes[i]
                   
        return len(B)
    
    def find_index(self, array_list, array, start, end):
        while start + 1 < end:
            mid = (start + end) // 2
            if array == array_list[mid]:
                return mid 
            elif array[0] > array_list[mid][0]:
                start = mid 
            else:
                end = mid
        
        if array_list[start][0] < array[0] or (array_list[start][0] == array[0] and array_list[start][1] < array[1]):
            return start       
        if array_list[end][0] < array[0] or (array_list[end][0] == array[0] and array_list[end][1] < array[1]):
            return end
        """

# 优化， 对高度进行插入，很难想到

class Solution:
    """
    @param: envelopes: a number of envelopes with widths and heights
    @return: the maximum number of envelopes
    """
    def maxEnvelopes(self, envelopes):
        if len(envelopes) <= 1:
            return len(envelopes)
        
        n = len(envelopes)

        envelopes = sorted(envelopes, key=lambda x:(x[0],-x[1]))
        # print(envelopes) #这里相当于求最长上升子序列
        heights = [nums[1] for nums in envelopes]
        
        # dp + 二分查找
        dp = [heights[0]] # 使用dp来保存高度信息
        length = 1
        
        for i in range(1, n):
            if heights[i] > dp[-1]:
                dp.append(heights[i])
            else:
                index = self.find_index(dp, heights[i], 0, len(dp) - 1)
                dp[index] = heights[i]
            # print(dp)
        return len(dp)
    
    def find_index(self, dp, h, start, end):
        while start + 1 < end:
            mid = (start + end) // 2
            if dp[mid] >= h:
                end = mid
            else:
                start = mid
        
        if dp[start] >= h:
            return start
        if dp[end] >= h:
            return end