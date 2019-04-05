'''
Given stones = [0,1,3,5,6,8,12,17]

There are a total of 8 stones.
The first stone at the 0th unit, second stone at the 1st unit,
third stone at the 3rd unit, and so on...
The last stone at the 17th unit.

Return true. The frog can jump to the last stone by jumping 
1 unit to the 2nd stone, then 2 units to the 3rd stone, then 
2 units to the 4th stone, then 3 units to the 6th stone, 
4 units to the 7th stone, and 5 units to the 8th stone.
'''

# 超时
class Solution:
    """
    @param stones: a list of stones' positions in sorted ascending order
    @return: true if the frog is able to cross the river or false
    """
    def canCross(self, stones):
        # stones = [0,1,3,5,6,8,12,17]
        n = len(stones)

        dp = {stones[i]:set() for i in range(len(stones))}
        dp[0] = set([0])

        for i in range(n):
            for step in dp[stones[i]]:
                # print(dp)
                if step - 1 + stones[i] in stones and step != 1:
                    dp[step - 1 + stones[i]].add(step - 1)
                if step + stones[i] in stones:
                    dp[step + stones[i]].add(step)
                if step + 1 + stones[i] in stones:
                    dp[step + 1 + stones[i]].add(step + 1)
                if len(dp[stones[n - 1]]) > 0:
                    return True
        
        return False

# 字典查找：通过
class Solution:
    def canCross(self, stones):

        # stones = [0,1,3,5,6,8,12,17]
        n = len(stones)

        dp = {stones[i]:set() for i in range(len(stones))}
        dp[0] = set([0])

        for i in range(n):
            for step in dp[stones[i]]:
                # print(dp)
                if step - 1 + stones[i] in dp and step != 1:
                    dp[step - 1 + stones[i]].add(step - 1)
                if step + stones[i] in dp:
                    dp[step + stones[i]].add(step)
                if step + 1 + stones[i] in dp:
                    dp[step + 1 + stones[i]].add(step + 1)
                if len(dp[stones[n - 1]]) > 0:
                    return True
        
        return False

# 空间换时间
# 
# 最后一步：如果可以跳到最后一个石头An-1， 考虑最后跳的一步L
# 青蛙一定是从某个位置Ai = An-1 - L 跳到最后一步的 
# 所以先考虑能否跳到Ai。
# 注意倒数第二跳只能是L，L-1，L+1
# 问题转化为 能否最后一跳L，L-1，L+1跳到Ai
# 设f[i][j] 表示青蛙能否最后一跳j跳到石头Ai
# 如果上一块石头是Ak = Ai - j 
# 可以通过一个哈希表（Ak - k）快速找到k
# f[i][j] = (f[k][j-1] or f[k][j] or f[k][j+1]) 
# | Ak = Ai - j 分别对应j-1，j，j+1跳到Ak 
# 应该枚举最后一跳的长度j 而不是k
# 因此无法用滚动数组优化 因为k不确定

# 注意：最后一跳最多是N-1 所以j的范围就可以确定
# 初始化：
# 只有一块石头 f[0][0] = True
# 只有两块石头 两者距离只能是1
# 由于第一步距离是1 f[1][1] = True，f[1][2...N-1] = False
# 答案： 如果f[N-1] 中有任何一个数是True 即为True

# 优化：用dicitonary
# f[Ai] = Si，枚举每一个在集合Si中的L，从石头i尝试往后跳L，L-1，L+1
# 如果跳了M距离后有一个石头j，则把M加到Sj中，
# 表示可以最后一步跳M到达石头j f[j][M] = True
class Solution:
    """
    @param stones: a list of stones' positions in sorted ascending order
    @return: true if the frog is able to cross the river or false
    """
class Solution:
    """
    @param stones: a list of stones' positions in sorted ascending order
    @return: true if the frog is able to cross the river or false
    """
    def canCross(self, stones):
        # stones = [0,1,3,5,6,8,12,17]
        n = len(stones)
        index_hash = {stones[i]:i for i in range(n)}

        # dp[i][j] 表示可以跳j步到石头Ai, 
        dp = [[False for j in range(len(stones))] for i in range(len(stones))]
        dp[0][0] = True 
        # for j in range(2, n):
            # dp[1][j] = False

        for i in range(1, len(stones)):
            stone = stones[i]
            for j in range(1, i+1):
                if self.canJump(dp, stones, i, j, index_hash):
                    dp[i][j] = True
            
        for j in range(len(stones)):
            if dp[len(stones) - 1][j] == True: 
                return True 
        return False

    def canJump(self, dp, stones, i, j, index_hash):
        stone_k = stones[i] - j
        if stone_k not in index_hash:
            return False
        
        k = index_hash[stone_k]
        if (j - 1 >= 0 and dp[k][j-1]) or dp[k][j] or (j + 1 <= i and dp[k][j+1]):
            return True
        
        return False

