# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rob(self, root: TreeNode | None) -> int:
        dp = {(None, True):0, (None, False):0}

        def helper(node, parent_skipped = True):
            if (node, parent_skipped) in dp:
                return dp[(node, parent_skipped)]
            total_skipped = helper(node.left, True)+ helper(node.right, True)
            total_unskipped = 0
            if parent_skipped:
                total_unskipped = node.val + helper(node.left, False)+ helper(node.right, False)

            dp[(node, parent_skipped)] = max(total_skipped, total_unskipped)
            return dp[(node, parent_skipped)]
            
        
        return helper(root)
