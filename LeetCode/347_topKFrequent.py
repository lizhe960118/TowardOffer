class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict_k = {}
        for i in range(len(nums)):
        	if not nums[i] in dict_k:
        		dict_k[nums[i]] = 1
        	else:
        		dict_k[nums[i]] = dict_k[nums[i]] + 1

        # print(dict_k.items())
        sorted_dict = sorted(dict_k.items(), key=lambda e: e[1],reverse=True)

        result = []
        for i in range(k):
        	result.append(sorted_dict[i][0])
        return result

if __name__ == '__main__':
	print(Solution().topKFrequent([1,1,1,2,2,3], 2))