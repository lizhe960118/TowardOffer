# def coinChange(coins, amount):
# 	"""
# 	:type coins: List[int]
# 	:type amount: int
# 	:rtype: int
# 	"""
# 	if not coins:
# 		return -1
# 	if not amount:
# 		return 0
# 	coins.sort(reverse = True)
# 	ans = coin_change(coins, 0, amount, 0)
# 	return ans if ans != float('inf') else -1
#
# def coin_change(coins, s, amount, count, min_ans):
# 	"""
# 	深度优先搜索树
# 	:param coins:硬币的组成[5. 2. 1]
# 	:param s: 当前遍历的层数[0, 1, 2]
# 	:param amount: 剩余硬币的数值
# 	:param count: 当前已经使用硬币的数量
# 	:return: 返回最后的最少使用硬币的数量
# 	"""
# 	# min_ans = float('inf')
# 	coin = coins[s]
# 	if s == len(coins) - 1:
# # 		最后一层
# 		if(amount % coin == 0):
# 			min_ans = min(min_ans, (count + amount // coin))
# 		return min_ans
# 	else:
# 		for k in range(amount // coin, -1, -1):
# 			if count + k < min_ans:
# 				min_ans = min(min_ans, coin_change(coins, s + 1, amount - k * coin, count + k))
# 	return min_ans

class Solution(object):
	def __init__(self):
		self.ans = float('inf')

	def coinChange(self, coins, amount):
		"""
		:type coins: List[int]
		:type amount: int
		:rtype: int
		"""
		if not coins:
			return -1
		if not amount:
			return 0
		coins.sort(reverse=True)

		def coin_change(coins, s, amount, count):
			"""
			深度优先搜索树
			:param coins:硬币的组成[5. 2. 1]
			:param s: 当前遍历的层数[0, 1, 2]
			:param amount: 剩余硬币的数值
			:param count: 当前已经使用硬币的数量
			:return: 返回最后的最少使用硬币的数量
			"""
			coin = coins[s]
			if s == len(coins) - 1:
				# 		最后一层
				if (amount % coin == 0) and (self.ans > (count + amount // coin)):
					self.ans = count + amount // coin
			else:
				for k in range(amount // coin, -1, -1):
					if count + k < self.ans:
						coin_change(coins, s + 1, amount - k * coin, count + k)

		coin_change(coins, 0, amount, 0)
		return self.ans if self.ans != float('inf') else -1

if __name__ == '__main__':
    print(Solution().coinChange([1, 2, 5],11))