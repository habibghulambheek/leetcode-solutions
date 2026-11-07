from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode | None) -> int:
        level = deque()
        level.appendleft((1, root))
        ans = 1
        while level:
            n = len(level)
            first =  level[0][0]
            ans = max(ans, level[-1][0] - level[0][0] + 1)
            for i in range(n):
                pos, node =  level.popleft()
                pos -= first
                if node.left:
                    level.append((2*pos, node.left))
                if node.right:
                    level.append((2*pos + 1, node.right))
        return ans
