# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        if not inorder or not postorder:
            return 
        root = TreeNode(postorder[-1])
        split_index = inorder.index(root.val)
        root.right = self.buildTree(inorder[split_index + 1::],postorder[split_index:len(postorder) - 1])

        root.left  = self.buildTree(inorder[:split_index],postorder[:split_index])

        return root