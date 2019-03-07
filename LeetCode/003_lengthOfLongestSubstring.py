class Solution(object):
    def lengthOfLongestSubstring(self,s):
        """
        :param s: str
        :return: int
        """
        if not s:#s is null
            return 0
        if len(s) <= 1:
            return len(s)
        locations = [-1 for i in range(256)]
        index = -1
        m = 0
        for i, v in enumerate(s):
            if locations[ord(v)] > index:
                index = locations[ord(v)]
            m = max(m, i - index)
            locations[ord(v)] = i
        return m

if __name__ == "__main__":
    # assert Solution().lengthOfLongestSubstring("abcda") == 4
    print(Solution().lengthOfLongestSubstring("pwwkew"))


