# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        ans = True
        def check_balance(node, height = 0):
            nonlocal ans
            if not node:
                return height
            if not ans:
                return None
            
            left_height  = check_balance(node.left, height+ 1)
            right_height = check_balance(node.right, height+ 1)
            if left_height == None or right_height == None:
                return None
            if abs(left_height - right_height) > 1:
                ans = False
            
            return max(left_height, right_height)
        check_balance(root)
        return ans