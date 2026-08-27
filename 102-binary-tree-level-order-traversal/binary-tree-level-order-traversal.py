from queue import Queue
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        levels = []

        queue = Queue()

        queue.put((root, 1))
        levels.append([root.val])
        while not queue.empty():
            node, h = queue.get()
            if node.left:
                queue.put((node.left, h + 1))
                if len(levels) < h + 1:
                    levels.append([])
                levels[h].append(node.left.val)
            
            if node.right:
                queue.put((node.right, h + 1))
                if len(levels) < h + 1:
                    levels.append([])
                levels[h].append(node.right.val)

        return levels