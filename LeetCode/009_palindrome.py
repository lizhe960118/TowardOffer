class Solution(object):
    def palindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        div = 1
        while(x / div > 10):
            div *= 10
        # div /= 100
        while(x > 0):
            l = x // div
            d = x % 10
            if l != d:
                return False
            # x = (x - l * div - d) // 10
            # div /= 100
            x %= div
            x //= 10
            div /= 100
        return True


if __name__ == "__main__":
    print(Solution().palindrome(1001))
