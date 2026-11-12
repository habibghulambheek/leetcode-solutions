# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        dp = {None: 0}
        ans =  root.val
        def helper(node):
            nonlocal ans
            if not node:
                return 0
            left = helper(node.left)
            right =  helper(node.right)
            
            
            # ans = max(ans , total)

            total = node.val
            if left >  right:
                if left > 0:
                    total += left
                
            else:
                if right > 0:
                    total += right     
            ans = max(ans,total, node.val + right + left)
            return total
        helper(root)
        return ans

            