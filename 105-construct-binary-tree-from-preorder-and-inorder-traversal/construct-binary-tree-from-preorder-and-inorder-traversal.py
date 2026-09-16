# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        if not preorder or not inorder:
            return
        root       =  TreeNode(preorder[0])
        split_idx  =  inorder.index(root.val)

        root.left  = self.buildTree(preorder[1:1 + split_idx], inorder[0:split_idx])
        root.right = self.buildTree(preorder[1 + split_idx::], inorder[split_idx + 1::])
        
        return root