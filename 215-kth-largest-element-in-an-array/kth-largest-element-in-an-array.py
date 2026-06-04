class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # min_heap = 3
        heap = nums[:k]
        heapq.heapify(heap)
        for x in nums[k:]:
            if heap[0] < x:
                heapq.heapreplace(heap,x)
        return heap[0]
        # k log n + n 