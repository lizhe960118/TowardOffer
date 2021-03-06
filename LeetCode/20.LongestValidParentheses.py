class Solution(object):
	def LongestValidParentheses(self,s):
		if not s:
			return 0
		length = len(s)
		dp = [0 for __ in range(length)]
		for i in range(1, length):
			if s[i] == ")":
				j = i - 1 - dp[i - 1]
				if j >= 0 and s[j] == "(":
					dp[i] = dp[i - 1] + 2
					if j - 1 >= 0:
						dp[i] += dp[j - 1]
		return max(dp)
