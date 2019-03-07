# 127 word ladder
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
    # beginWord为开始的单词，endWord为目标单词，wordList为可供转换的元素组成的列表
        def construct_dict():
            d = {}
            for word in wordList:
                for i in xrange(len(word)):
                    s = word[:i] + "_" + word[i+1:]
                    d[s] = d.get(s, []) + [word]
            return d

        def bfs(begin, target, d):
            queue, visited = [(begin, 1)], set()
            while len(queue) > 0:
                word, steps = queue.pop(0)
                if word not in visited:
                    visited.add(word)
                    if word == target:
                        return steps
                    for i in xrange(len(word)):
                        s = word[:i] + "_" + word[i+1:]
                        for j in d.get(s, []):
                            # 如果j在visited中，说明j已经被访问过了，不需要再次进行访问。
                            if j not in visited:
                                queue.append((j, steps+1))
            return 0

        d = construct_dict()
        return bfs(beginWord, endWord, d)