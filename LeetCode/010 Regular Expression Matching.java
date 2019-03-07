dp[0][0] = true
1.当前字符匹配
p.charAt(j) == s.charAt(i)
dp[i][j] = dp[i - 1][j - 1]
2.当前字符为"."
p.charAt(j) == "."
dp[i][j] = dp[i - 1][j - 1]
3.当前字符为"*"
p.charAt(j) == "*":
	1)p.charAt(j) ！= s.charAt(i)：dp[i][j] = dp[i][j-2]
	2)p.charAt(j-1) == s.charAt(i-1) || p.charAt(j - 1) == ".":
		dp[i][j] = dp[i][j-1]	//匹配一个字符 'aa' 'a*'
			|| dp[i - 1][j] //匹配两个字符 'aaa' 'a*'
			|| dp[i][j - 2] //匹配0个字符 'aa' 'a*'