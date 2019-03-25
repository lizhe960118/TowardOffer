class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        num = ""
        tmp_stack = [["", 1]]
        for c in s:
        	if c in '0123456789':
        		num += c
        	elif c == '[':
        		tmp_stack.append(['', int(num)])
        		num = ''
        	elif c == ']':
        		ss, k_num = tmp_stack.pop()
        		tmp_stack[-1][0] += k_num * ss
        	else:
        		tmp_stack[-1][0] += c
        result, _ = tmp_stack.pop()
        return result

if __name__ == '__main__':
	print(Solution().decodeString('3[a]2[bc]'))