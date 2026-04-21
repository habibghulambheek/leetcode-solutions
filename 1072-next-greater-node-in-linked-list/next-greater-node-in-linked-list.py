# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        ans = []
        stack = []
        i = 0
        while head:
            while stack and stack[-1][1] < head.val:
                idx = stack.pop()
                ans[idx[0]] = head.val
            ans.append(0)
            stack.append((i,head.val))
            i+= 1
            head = head.next
        return ans