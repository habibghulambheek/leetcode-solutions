# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        max_level = 0
        ans = []
        def visit_nodes(node, level = 0):
            nonlocal max_level
            nonlocal ans
            if not node:
                return 
            level += 1
            if max_level < level:
                max_level = level
                ans.append(node.val)
            visit_nodes(node.right, level)
            visit_nodes(node.left, level)
        visit_nodes(root)
        return ans