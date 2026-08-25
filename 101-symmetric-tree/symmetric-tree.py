# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        
        def check_symmetry(left, right):
            if left == None and right == None:
                return True
            elif (left == None) or (right == None) or (left.val != right.val):
                return False
            if not check_symmetry(left.right, right.left):
                return False
            if not check_symmetry(left.left, right.right):
                return False
            return True
        
        return check_symmetry(root.left, root.right)
