class Solution(object):
	def wordBreak(s, wordDict):
		if len(wordDict) == 0:
			return false
		dp = [0 for _ in range(len(s))]

		for i in range(len(s)):
			for j in range(len(wordDict)):
				len_j = len(wordDict[j])
				if(i + 1 >= len_j and wordDict[j] == s[i + 1 - len_j: i + 1] and
					(i + 1 - len_j == 0 or dp[i - len_j] == 1)):
					dp[i] = 1
					break

		return dp(len(s) - 1)