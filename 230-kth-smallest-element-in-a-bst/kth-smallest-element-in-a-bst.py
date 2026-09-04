# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return
        def return_inorder(node, ans = []):
            if not node:
                return
            return_inorder(node.left, ans)
            ans.append(node.val)
            return_inorder(node.right, ans)

        ans = []
        return_inorder(root, ans)

        return ans[k-1]
