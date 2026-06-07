from collections import Counter
import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        num_counts = Counter(nums)
        # print(num_counts)

        heap = []
        for key in num_counts:
            if len(heap) < k:
                heapq.heappush(heap,(num_counts[key], key))
            else:
                if heap[0][0] < num_counts[key]:
                    heapq.heappop(heap)
                    heapq.heappush(heap,(num_counts[key], key))
            # print(heap)
        return [x for (y,x) in heap]