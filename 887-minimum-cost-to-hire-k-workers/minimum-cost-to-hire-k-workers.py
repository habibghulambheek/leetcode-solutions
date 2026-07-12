class Solution(object):
    def mincostToHireWorkers(self, quality, wage, k):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type k: int
        :rtype: float
        """
        n = len(quality)
        ratios =  sorted([(float(wage[i])/quality[i], quality[i]) for i in range(n)])

        best_cost = float("inf")
        max_heap = []
        quality_sum =  0

        for ratio, q in ratios:
            heapq.heappush(max_heap, -q)
            quality_sum += q   
            if len(max_heap) == k:
                cost = ratio * quality_sum
                best_cost = min(best_cost, cost)
                quality_sum +=  heapq.heappop(max_heap)
        return best_cost
