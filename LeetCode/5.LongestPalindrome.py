class Solution(object):
    def longestPalindrome(self, s):
        """

        :param s : str
        :return: str
        """
        maxLen = 0
        index = 0
        length = len(s)
        for i in range(length):
            len1 = extendPalindrome(self, s, i, i)
            # sume odd length, try to extend Palindrome as possible
            len2 = extendPalindrome(self, s, i, i + 1)
            if maxLen < max(len1, len2):
                if len1 > len2:
                    index = i - len1 // 2
                else:
                    index = i - len2 // 2 + 1
                maxLen = max(len1, len2)
        return s[index: index + maxLen]


def extendPalindrome(self, s, i, j):
    while (i >= 0) & (j < len(s)):
        if s[i] == s[j]:
            i -= 1
            j += 1
        else:
            break
    return j - i - 2 + 1


if __name__ == "__main__":
    print(Solution().longestPalindrome("aba"))
    print(Solution().longestPalindrome("abba"))
    print(Solution().longestPalindrome("xaba"))
    print(Solution().longestPalindrome("xabba"))
