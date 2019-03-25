def findKthLargest(nums, k):
	if not nums or len(nums) == 0:
		return 0
	left = 0
	right = len(nums) - 1
	while True:
		pos = partition(nums. left, right)
		if (pos + 1) == k:
			return nums[pos]
		elif (pos + 1) > k:
			right = pos - 1
		else:
			left = pos + 1

def partition(nums, left, right):
	pivot = nums[left]
	l = left + 1
	r = right
	while l <= r:
		if pivot > nums[l] and pivot < nums[r]:
			nums[l], nums[r] = nums[r], nums[l]
			#保证左边的数比pivot大，右边的数比pivot小
			l , r = l + 1, r - 1
		if pivot <= nums[l]:
			l += 1
		if pivot >= nums[r]:
			r -= 1
	nums[left], nums[r] = nums[r], nums[left]
	return r
	"""
	** 
	*    3, 2, 1, 5, 6, 4   k=3
	*    0, 1, 2, 3, 4, 5

	pivot:3 nums:[3, 2, 1, 5, 6, 4]
	---> [3, 4, 6, 5, 1, 2] 
	---> [5, 4, 6, 3, 1, 2] l=r=3 return 3
	---> nums[3] 为 第 3 + 1 大的数
	right= pos - 1 = 3 - 1 = 2
	left = 0
	nums:[5, 4, 6, 3, 1, 2] 
	pivot:5 
	--->[5, 6, 4, 3, 1, 2] l =2, r = 1
	--->[6, 5, 4, 3, 1, 2] return 1
	---> nums[1] 为 第 1 + 1 大的数
	1+1 < 3:
	right=2, left= pos+1 = 2
	nums:[6. 5. 4. 3. 1. 2]
	pivot:5
	---> l = 3  r = 2 return 2
	---> nums[2] 为 第 3 大的数
	"""