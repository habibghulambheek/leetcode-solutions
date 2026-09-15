# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode | None):
        self.stack = []
        node = root

        while node:
            self.stack.append(node)
            node = node.left
    

    def next(self) -> int:
        node = self.stack.pop()
        temp = node
        temp = temp.right
        
        while temp:
            self.stack.append(temp)
            temp = temp.left
        return node.val

    def hasNext(self) -> bool:
        if self.stack:
            return True    
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()