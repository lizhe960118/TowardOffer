# 只准交易一次
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #贪心算法
        n = len(prices)
        if n == 0:
            return 0
        my_buy = -prices[0]
        profit = 0
        
        for i in range(1, n):
            # 当前值有两种选择，要么买入，要么卖出
            my_buy = max(my_buy, -prices[i]) # 当前值买入，花费最少，-2 > -9
            profit = max(profit, prices[i] + my_buy) # 当前值卖出，计算收入
        return profix

# 可以完成多次交易
class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        if n == 0:
            return 0
        buy = -prices[0]
        sell = 0 
        for i in range(1, n):
            # 同样有两种选择，买入或者卖出
            # 买入：花费最少。最开始sell=0,即花费-prices[i], 之后, 买入的花费为sell - prices[i]
            buy = max(buy, sell - prices[i]) # buy都是负值
            # 当前值卖出，price[i]减去买入花的前
            sell = max(sell, prices[i] + buy)
        return sell 

    def maxProfit(self, prices):
        n = len(prices)
        if n == 0:
            return 0
        buy = prices[0]
        sell = 0
        for i in range(1, n):
            buy = min(buy, prices[i] - sell) # 这是我买股票花的钱
            sell = max(sell, prices[i] - buy)
        return sell

# 最多完成两次交易
class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        if n == 0:
            return 0
        buy_1 = -prices[0]
        sell_1 = 0
        buy_2 = -prices[0]
        sell_2 = 0

        for i in range(1, n):
            buy_1 = max(buy_1, -prices[i])
            sell_1 = max(sell_1, prices[i] + buy_1)
            buy_2 = max(buy_2, sell_1 - prices[i])
            sell_2 = max(sell_2, buy_2 + prices[i])
        return max(sell_1, sell_2)

# 含一天的冷冻期，卖出后的一天不能交易，可以多次交易

# 这是股票系列问题中目前来看最难的一个，不过有了前面几个问题的思路，这个问题求解起来非常容易。
# 首先，我们看到问题中提到了三种状态buy、sell和cooldown，那么我们脑中的第一个想法就是通过动态规划来解。

# 如果我们index:i天为冷冻期，那么只能说明index:i-1天卖掉了股票，
# 那么i天的收益和i-1天是一样的
# cooldown[i] = sell[i-1]

# 如果我们考虑index:i天卖出，要求利润最大的话。则index:i-1之前就持有股票。
# 一种情况就是index:i-1当天买入了股票，我们在这一天卖出比sell[i-1]获利多
# 另一种情况是index:i-1天已经可以卖出，sell[i-1]记录了这种情况
# sell[i] = max(sell[i-1], buy[i-1] + prices[i])

# 如果我们考虑index:i天买入，要求利润最大的话。则index:i-1之前就不持有股票。
# 我们要考虑哪天买，
# 一种可能是index:i-1天是冷冻期
# 另一种可能是index:i-1已经可以买入，buy[i-1]记录这种情况，
# buy[i] = max(buy[i-1], cooldown[i-1]-prices[i])

# 我们第一天不可能卖出或者冻结，那么这两个sell[0]=0 cooldown[0]=0，
# 但是我们第一天可以买入啊，所以buy[0]=-prices[0]。
# 还有一点要注意的就是，我们一定是最后一天卖出或者最后一天冻结利润最大。

class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        if n == 0:
            return 0
        buy = -prices[0]
        sell = 0
        cooldown = 0
        
        for i in range(1, n):
            buy = max(buy, cooldown - prices[i]) # 如果当前买入，则只能有cooldown转移过来
            cooldown = sell 
            sell = max(sell, buy + prices[i])

        return max(sell, cooldown)