# class Solution(object):
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         tmp = ['#']
#         for i in range(len(s)):
#             tmp.append(s[i:i+1])
#             tmp.append('#')
#         s_new = ("").join(tmp)
#         print(s_new)
#         mid = len(s_new) // 2
#         max_length = 0
#         for i in range(1, mid):
#             cur = s_new[i: len(s_new) - i]
#             if self.isPalindrome(cur):
#                 max_length = max(max_length, len(cur))
#         return max_length // 2

#     def isPalindrome(self, s):
#         return s == s[::-1]

# if __name__ == '__main__':
#     print(Solution().longestPalindrome("abccccdd"))

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict_tmp = {}
        for i in range(len(s)):
            cur_char = s[i:i+1]
            if cur_char not in dict_tmp:
                dict_tmp[cur_char] = 1
            else:
                dict_tmp[cur_char] += 1

        max_length = 0
        flag = 0
        for index, value in dict_tmp.items():
            if value % 2 == 1:
                flag = 1
                max_length += value - 1
            else:
                max_length += value

        return max_length + flag