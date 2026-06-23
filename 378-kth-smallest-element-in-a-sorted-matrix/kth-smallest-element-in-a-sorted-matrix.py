class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap  = []
        ans   = []
        # seeding
        n = len(matrix)
        for j in range(min(k,n)):
            heapq.heappush(heap, (matrix[0][j], 0, j))
        while heap and len(ans) < k:
            val, i, j = heapq.heappop(heap)
            ans.append(val)
            if (i + 1) < n:
                heapq.heappush(heap, (matrix[i+1][j], i + 1, j))
        return ans[-1]