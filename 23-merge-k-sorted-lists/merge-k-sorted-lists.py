# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        if not lists:
            return None
        heap = []
        head = None
        k = len(lists)
        for i in range(k):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val,i,lists[i]))
        while heap:
            val,idx ,node = heapq.heappop(heap)
            if node.next:
                heapq.heappush(heap, (node.next.val,idx,node.next))
            if head:
                ans.next = node
                ans = ans.next
                ans.next = None
            else:
                head = node
                ans = node
                ans.next = None

        return head