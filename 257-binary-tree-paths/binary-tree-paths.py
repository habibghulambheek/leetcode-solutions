# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        if not root:
            return []

        stack = []
        stack.append((root, str(root.val)))
        paths = []
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                
                paths.append(path)
                continue

            if node.left:
                stack.append((node.left, path +"->" + str(node.left.val)))
            if node.right:
                stack.append((node.right, path +"->" + str(node.right.val)))
        
        return paths
