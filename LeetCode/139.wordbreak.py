# 139 word break.py
class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        return bfs(self, s, wordDict)

def bfs(self, s, wordDict):
    bfs = []
    visited = set()
    bfs.append(0)
    while len(bfs) > 0 :
        start = bfs.pop(0)
#         start用来记录起始点
        if start not in visited:
            visited.add(start)
            for j in range(start+1, len(s) + 1):
#                 j用来分割字符
                word = s[start:j]
                if word in wordDict:
#             如果当前分割情况在字典中，将j保存到visited中，下一次pop出来作为start
                    bfs.append(j)
                    if j == len(s):
                        return True
    return False
    