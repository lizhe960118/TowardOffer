def sortColors(nums):
	"""
	:type nums: List[int]
	:rtype: void Do not return anything, modify nums in-place instead.
	"""
	start = 0
	mid = 0
	end = len(nums) - 1
	while (mid <= end):
		if nums[mid] == 2:
			nums[mid], nums[end] = nums[end], nums[mid]
			end = end - 1
		elif nums[mid] == 1:
			mid = mid + 1
		elif nums[mid] == 0:
			nums[start], nums[mid] = nums[mid], nums[start]
			mid = mid + 1
			start = start + 1

if __name__ == '__main__':
	print(sortColors([1]))