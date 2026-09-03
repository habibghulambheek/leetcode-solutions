# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], max_val = None, min_val = None) -> bool:
        if not root:
            return True
        
        if min_val is not None and root.val <= min_val:
            return False
        if max_val is not None and root.val >= max_val:
            return False

        return (self.isValidBST(root.right, max_val, root.val)
        and self.isValidBST(root.left ,root.val, min_val))