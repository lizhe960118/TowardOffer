# 1.BFS
from queue import Queue
def canFinish(numCourses, prerequisites):
	len_prerq = len(prerequisites)
	graph = [[] for _ in range(numCourses)]
	degree = [0 for _ in range(numCourses)]
	count = 0
	q = Queue()

	for i in range(len_prerq):
		degree[prerequisites[i][0]] += 1
		graph[prerequisites[i][0]].append(prerequisites[i][1])

	for i in range(len(degree)):
		if (degree[i] == 0):
			q.put(i)
			count += 1

	while(q.qsize() != 0):
		course = q.get()
		for i in range(len(graph[course])):
			pointer = graph[course][i]
			degree[pointer] -= 1
			if(degree[pointer] == 0):
				q.put(pointer)
				count += 1
	return True if count == numCourses else False

# DFS
"""
def canFinish(numCourses, prerequisites):
	graph = [[] for _ in range(numCourses)]
	visited = [False for _ in range(numCourses)]
	for i in range(len(prerequisites)):
		graph[prerequisites[i][1]].append(prerequisites[i][0])
	for i in range(numCourses):
		if not dfs_find(graph, visited, i):
			return False
	return True

def dfs_find(graph, visited, course):
	if visited[course]:
		return False
	else:
		visited[course] = True

	for i in range(len(graph[course])):
		if not dfs_find(graph, visited, graph[course][i]):
			return False

	visited[course] = False
	return True
"""

if __name__ == "__main__":
	print(canFinish(2, [[1,0],[0,1]]))