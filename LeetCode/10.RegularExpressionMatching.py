class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = len(s)
        n = len(p)
        dp = [[False for i in range(n + 1)] for i in range(m + 1)]
        dp[m][n] = True
        for i in range(n - 1, -1, -1):
            if p[i] == '*':
                dp[m][i] = dp[m][i + 1]
            elif i + 1 < n and p[i + 1] == '*':
                dp[m][i] = dp[m][i + 1]
            else:
                dp[m][i] = False
        for i in range(m - 1, -1, -1):
            for j in range(n -1, -1, -1):
                if p[j] == '*':
                    if j - 1 >= 0 and p[j - 1] != '*':
                        dp[i][j] = dp[i][j + 1]
                    else:
                        return False
                elif j + 1 < n and p[j + 1] == '*':
                    if s[i] == p[j] or p[j] == '.':
                        dp[i][j] = dp[i][j + 2] or dp[i + 1][j] or dp[i + 1][j + 2]
                    else:
                        dp[i][j] = dp[i][j + 2]
                else:
                    if s[i] == p[j] or p[j] == '.':
                        dp[i][j] = dp[i + 1][j + 1]
                    else:
                        dp[i][j] = False
        return dp[0][0]

if __name__ == '__main__':
    # print(Solution().isMatch("aa", "a") == False)
    # print(Solution().isMatch("aa", "aa") == True)
    # print(Solution().isMatch("aaa", "aa") == False)
    print(Solution().isMatch("aa", "a*") == True)
    print(Solution().isMatch("aa", ".*") == True)
    print(Solution().isMatch("ab", ".*") == True)
    print(Solution().isMatch("aab", "c*a*b") == True)