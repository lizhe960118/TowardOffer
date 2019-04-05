#
# @lc app=leetcode id=684 lang=python3
#
# [684] Redundant Connection
#
# https://leetcode.com/problems/redundant-connection/description/
#
# algorithms
# Medium (50.67%)
# Total Accepted:    44.4K
# Total Submissions: 87.6K
# Testcase Example:  '[[1,2],[1,3],[2,3]]'
#
# 
# In this problem, a tree is an undirected graph that is connected and has no
# cycles.
# 
# The given input is a graph that started as a tree with N nodes (with distinct
# values 1, 2, ..., N), with one additional edge added.  The added edge has two
# different vertices chosen from 1 to N, and was not an edge that already
# existed.
# 
# The resulting graph is given as a 2D-array of edges.  Each element of edges
# is a pair [u, v] with u < v, that represents an undirected edge connecting
# nodes u and v.
# 
# Return an edge that can be removed so that the resulting graph is a tree of N
# nodes.  If there are multiple answers, return the answer that occurs last in
# the given 2D-array.  The answer edge [u, v] should be in the same format,
# with u < v.
# Example 1:
# 
# Input: [[1,2], [1,3], [2,3]]
# Output: [2,3]
# Explanation: The given undirected graph will be like this:
# ⁠ 1
# ⁠/ \
# 2 - 3
# 
# 
# Example 2:
# 
# Input: [[1,2], [2,3], [3,4], [1,4], [1,5]]
# Output: [1,4]
# Explanation: The given undirected graph will be like this:
# 5 - 1 - 2
# ⁠   |   |
# ⁠   4 - 3
# 
# 
# Note:
# The size of the input 2D-array will be between 3 and 1000.
# Every integer represented in the 2D-array will be between 1 and N, where N is
# the size of the input array.
# 
# 
# 
# 
# 
# Update (2017-09-26):
# We have overhauled the problem description + test cases and specified clearly
# the graph is an undirected graph. For the directed graph follow up please see
# Redundant Connection II). We apologize for any inconvenience caused.
# 
#
class graph_node(object):
    def __init__(self, val):
        self.val = val
        self.neighbors = set()

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        graph = self.build_graph(n, edges)

        for i in range(n-1, -1, -1):
            graph = self.graph_remove_edge(graph, edges[i])
            if self.isTree(graph):
                return edges[i]
            else:
                graph = self.graph_add_edge(graph, edges[i])
        
        return None

    def graph_remove_edge(self, graph, edge):
        u, v = edge
        graph[u].neighbors.remove(v)
        graph[v].neighbors.remove(u)
        return graph

    def graph_add_edge(self, graph, edge):
        u, v = edge
        graph[u].neighbors.add(v)
        graph[v].neighbors.add(u)
        return graph
    
    def build_graph(self, n ,edges):
        graph = {}
        for i in range(1, n+1):
            graph[i] = graph_node(i)
        for edge in edges:
            graph = self.graph_add_edge(graph, edge)    
        return graph
        
    def isTree(self, graph):
        visited = [False for i in range(len(graph))]
        self.count_visited = 0
        flag = self.checkCircle(1, 0, graph, visited)
        return flag and (len(graph) == self.count_visited)
    
    def checkCircle(self, cur_node, prev_node, graph, visited):
        if visited[cur_node - 1]:
            return False
             
        visited[cur_node - 1] = True
        self.count_visited += 1
        for neighbor in graph[cur_node].neighbors:
            if neighbor == prev_node:
                continue
            visited[neighbor - 1] == True
            if not self.checkCircle(neighbor, cur_node, graph, visited):
                return False
                
        return True
