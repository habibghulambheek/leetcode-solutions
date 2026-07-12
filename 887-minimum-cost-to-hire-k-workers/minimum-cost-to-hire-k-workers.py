import heapq

class Solution(object):
    def mincostToHireWorkers(self, quality, wage, k):
        n = len(quality)
        ratios = sorted([(float(wage[i])/quality[i], quality[i]) for i in range(n)])

        best_cost = float("inf")
        max_heap = []
        quality_sum = 0

        for ratio, q in ratios:
            quality_sum += q
            heapq.heappush(max_heap, -q)

            if len(max_heap) > k:
                quality_sum += heapq.heappop(max_heap)   # fixed: += not -=
            if len(max_heap) == k:
                cost = ratio * quality_sum
                best_cost = min(best_cost, cost)
        return best_cost