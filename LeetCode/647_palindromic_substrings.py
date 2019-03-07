class Solution(object):
    def countSubstings(self, s):
        """
        :type s: str
        :rtype:int
        """
        # 返回一个数组，对应位置为以i为中心的最长回文字符串半径
        p = self.manachar(s)
        print(p)
        count_num = 0
        for p_num in p:
            count_num += p_num // 2
        return count_num

    def manachar(self, s):
        s_new = ''
        for word in s:
            s_new += '#' + word
        s_new = '$' + s_new + '#' + '&'
        print(s_new)
        len_s_new = len(s_new)
        p = [0 for _ in range(len_s_new)]
        # max_substring_len, max_substring_pos = -1, -1
        idx, mx = 0, 0
        for i in range(1, len_s_new - 1):
            if (i < mx):
                p[i] = min(p[2 * idx - i], mx - i)
            else:
                p[i] = 1

            # while((i + p[i] < len_s_new)and (s_new[i - p[i]] == s_new[i +
            # p[i]])):if p_num > 1
            while(s_new[i - p[i]] == s_new[i + p[i]]):
                p[i] += 1

            if i + p[i] > mx:
                mx = i + p[i]
                idx = i

            # if p[i] - 1 > max_substring_len:
            #     max_substring_len = p[i] - 1
            #     max_substring_pos = i

        # print(max_substring_pos, max_substring_len)
        # istart = (max_substring_pos - max_substring_len - 1) // 2

        return p


if __name__ == '__main__':
    s = "abc"
    print(s)
    sub = Solution().countSubstings(s)
    print(sub)
