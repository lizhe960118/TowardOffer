class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]

        Input:
		[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

		Output:
		[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
        """
        # sort people by height
        people.sort()

        index = [i for i in range(len(people))]
        result = [None for _ in range(len(people))]

        while people:
        	cur_element = people.pop(0)
        	stack = [cur_element]
        	while(people and people[0][0] == stack[0][0]):
        		stack.append(people.pop(0))

        	while stack:
        		cur_element = stack.pop(-1)
        		result[index.pop(cur_element[1])] = cur_element
        return result

if __name__ == '__main__':
	print(Solution().reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))