class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = [0]
        # i >> 1 相当于将计算 i 中除最后一位以外1的个数
        # i % 2 计算 i 最后一位是否为1
        for i in range(1, num+1):
            result.append(result[i >> 1] + (i % 2))
        return result