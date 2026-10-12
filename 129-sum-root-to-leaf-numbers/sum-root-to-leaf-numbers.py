# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        
        ans = 0

        def helper(node, number = 0):
            nonlocal ans
            if not node:
                return
            
            number = (number * 10) + node.val
            if not node.left and not node.right:
                ans += number
                return
            helper(node.right, number) 
            helper(node.left , number)

        helper(root)
        return ans