# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        change_direction = False

        queue = deque()
        queue.append(root)

        ans = []
        while queue:
            row = []

            for _ in range(len(queue)):
                node = queue.popleft()
                row.append(node.val)
       
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if change_direction:
                row.reverse()
            ans.append(row)
            change_direction = not change_direction
        return ans