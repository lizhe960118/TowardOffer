class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        res_store = []

        flag = 1

        if num < 0:
            num = -num
            flag = -1

        while num != 0:
            next_num = num // 7
            st_num = num % 7
            res_store.append(str(st_num))
            num = next_num

        if flag == -1:
            res_store.append("-")

        result = "".join(res_store)

        return result[::-1]