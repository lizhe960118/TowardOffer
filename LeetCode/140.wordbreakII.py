# 140 word break II.py
from functools import reduce
class Solution(object):
	def wordBreak(self, s, wordDict):
		self.val = []
		self.bfs(s, wordDict, "")
		return self.val

	def bfs(self, s, wordDict, ret):
		if len(s) == 0:
			ret = ret.strip()
			ret = ret.split()[::-1]
			ret = reduce(lambda x,y: x + " " + y, ret, "")
			self.val.append(ret.strip())

		else:
			bfs = []
			visited = set()
			bfs.append(0)
			while len(bfs) > 0:
				start = bfs.pop(0)
				if start not in visited:
					visited.add(start)
					for j in range(start+1, len(s) + 1):
						word = s[start:j]
						if word in wordDict:
							bfs.append(j)
							if j == len(s):
								self.bfs(s[:start], wordDict, ret + " " + word)
