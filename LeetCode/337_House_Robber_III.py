# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        result = max(self.subRob(root))
        return result
    
    def subRob(self, root):
        left_val = [0, 0]
        right_val = [0, 0]
        tmp_result = [0, 0]
        if not root:
            return [0, 0]
        if root.left:
            left_val = self.subRob(root.left)
        if root.right:
            right_val = self.subRob(root.right)        
        # not rob root
        tmp_result[0] = max(left_val[0], left_val[1]) + max(right_val[0], right_val[1])
        # rob root
        tmp_result[1] = root.val + left_val[0] + right_val[0]
        return tmp_result