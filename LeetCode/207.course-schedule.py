#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#
# https://leetcode.com/problems/course-schedule/description/
#
# algorithms
# Medium (37.02%)
# Total Accepted:    196K
# Total Submissions: 529.6K
# Testcase Example:  '2\n[[1,0]]'
#
# There are a total of n courses you have to take, labeled from 0 to n-1.
# 
# Some courses may have prerequisites, for example to take course 0 you have to
# first take course 1, which is expressed as a pair: [0,1]
# 
# Given the total number of courses and a list of prerequisite pairs, is it
# possible for you to finish all courses?
# 
# Example 1:
# 
# 
# Input: 2, [[1,0]] 
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# 
# Example 2:
# 
# 
# Input: 2, [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you
# should
# also have finished course 1. So it is impossible.
# 
# 
# Note:
# 
# 
# The input prerequisites is a graph represented by a list of edges, not
# adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.
# 
# 
#
class graph_node(object):
    def __init__(self, value):
        self.val = value
        self.neighbors = []

import collections
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses

        graph, in_degrees = self.build_graph(numCourses, prerequisites)

        q = collections.deque()
        count = 0

        for i in range(n):
            if in_degrees[i] == 0:
                q.append(graph[i])
                count += 1
        
        while q:
            node = q.popleft()
            for neighbor in node.neighbors:
                in_degrees[neighbor.val] -= 1
                if in_degrees[neighbor.val] == 0:
                    q.append(neighbor)
                    count += 1
        
        return count == n     
        
    def build_graph(self, n, edges):
        graph = {}
        in_degrees = [0 for i in range(n)]
        for i in range(n):
            graph[i] = graph_node(i)
        for edge in edges:
            value_u, value_v = edge
            in_degrees[value_u] += 1
            u, v = graph[value_u], graph[value_v]
            v.neighbors.append(u)
        return graph, in_degrees

