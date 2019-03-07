class Solution(object):
	"""docstring for Solution"""
	def foursum(self, nums,target):
		"""
		:type nums:List[int]
		:type target:int
		:rtype:List[List[int]] 
		"""
		if len(nums) < 4:
			return []
		result = set()
		sumsIndexes = {}
		for i in range(len(nums)):
			for j in range(i + 1,len(nums)):
				temp =  nums[i] + nums[j]
				if temp in sumsIndexes:
					sumsIndexes[temp].append[(i,j)]
				else:
					sumsIndexes[temp] = [(i,j)]
		for i in range(len(nums)):
			for j in range(i + 1,len(nums)):
				temp = nums[i] + nums[j]
				SumNeeded = target - temp
				if SumNeeded in sumsIndexes:
					for index in sumsIndexes[SumNeeded]:
						if index[0] > j:
							result.add(tuple(sorted(nums[i],nums[j],nums[index[0]],nums[index[1]])))
		result = [list(l) for l in result]
		return result