# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        count = 0
        def find_paths(node,running_sum = 0, prefix = {0:1}):

            nonlocal count
            if not node:
                return


            running_sum += node.val 

            if  (running_sum - targetSum) in prefix:
                count += prefix[(running_sum - targetSum)] 
            
            prefix[running_sum] = prefix.get(running_sum, 0) + 1
            find_paths(node.left, running_sum, prefix.copy())
            find_paths(node.right, running_sum, prefix.copy())
        find_paths(root)
        return count
            