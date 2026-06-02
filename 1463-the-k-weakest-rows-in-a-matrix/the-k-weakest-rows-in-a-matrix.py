import heapq
class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        count =  []
        idx  = 0
        for row in mat:
            count.append((sum(row), idx))
            idx += 1
        
        # print(count)

        heapq.heapify(count)

        result = []
        for i in range(k):
            value =  heapq.heappop(count)
            result.append(value[1])
        return result
