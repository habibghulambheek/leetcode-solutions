# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        def check_sum(node, _sum = 0):
            _sum  = _sum + node.val

            if node.left == None and node.right == None:
                return _sum == targetSum
            
            if node.left and check_sum(node.left, _sum ):
                return True
            if node.right and check_sum(node.right, _sum ):
                return True
            return False
        return check_sum(root)