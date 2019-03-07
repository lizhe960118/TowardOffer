# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.result = []
        self.find_path(root, sum, [])
        return self.result

    def find_path(self, node, sum, tmp):
        if node is None:
            return
        if (node.val == sum) and (node.left is None) and (node.right is None):
            self.result.append(tmp + [node.val])
        else:
            self.find_path(node.left, sum - node.val, tmp + [node.val])
            self.find_path(node.right, sum - node.val, tmp + [node.val])   