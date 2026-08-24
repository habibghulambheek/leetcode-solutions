# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, a, b):
        """
        :type a: Optional[TreeNode]
        :type b: Optional[TreeNode]
        :rtype: bool
        """

        
        def isSame(p, q):
            # print(p,q)
            if p == None and q !=None:
                return False
            elif q == None and p != None:
                return False
            elif q == None and p == None:
                return True
            if p.val != q.val:
                return False
            sameLeft = isSame(p.left, q.left)

            if  sameLeft == False:
                return False

            sameRight = isSame(p.right, q.right)

            if  sameRight == False:
                return False

            return True
        return isSame(a, b)