# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None
        def LCA(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'):
            nonlocal ans

            found = set()
            if not root:
                return found
            if root == p:
                found = {p}
            if root == q:
                found = {q}

            found.update(LCA(root.left , p, q))
            if ans:
                return found
            found.update(LCA(root.right, p, q))
            if ans:
                return found
            if p in found and q in found:
                ans = root
            return found

        LCA(root, p, q)
        return ans