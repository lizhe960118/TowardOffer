#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#
# https://leetcode.com/problems/binary-tree-preorder-traversal/description/
#
# algorithms
# Medium (50.59%)
# Total Accepted:    315.3K
# Total Submissions: 623.3K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the preorder traversal of its nodes' values.
# 
# Example:
# 
# 
# Input: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
# 
# Output: [1,2,3]
# 
# 
# Follow up: Recursive solution is trivial, could you do it iteratively?
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        #  root, left, right
        if root is None:
            return []
        
        stack = []

        result = []
        
        
        cur_node = root 
        while stack or cur_node:
            if cur_node :
                stack.append(cur_node)
                result.append(cur_node.val)
                cur_node = cur_node.left 
            else:
                cur_node = stack.pop()
                # if cur_node.right: 这里不需要判断，否则进入死循环
                cur_node = cur_node.right          

        return result
