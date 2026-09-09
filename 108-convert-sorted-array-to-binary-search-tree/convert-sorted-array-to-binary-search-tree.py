# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        mid_idx = (n// 2)
        
        def make_tree(start, end):
            if end < start or start > end:
                return
            
            mid_idx = start + (end - start)//2 
            root = TreeNode(nums[mid_idx])

            root.left  = make_tree(start, mid_idx - 1)
            root.right = make_tree(mid_idx + 1, end)
            
            return root

        return make_tree(0, n-1)

    