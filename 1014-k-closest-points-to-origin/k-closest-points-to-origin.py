import heapq
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        def euclidean_distance(x,y):
            return  ((0-x)**2 + (0-y)**2)**(1.5)
        
        heap = []
        for idx in range(len(points)):
            if len(heap) < k:
                heapq.heappush(heap, (-euclidean_distance(points[idx][0], points[idx][1]),idx))
            else:
                distance = euclidean_distance(points[idx][0], points[idx][1])
                # print(distance,idx)
                if abs(heap[0][0]) > distance:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (-distance,idx))
            # print(heap)
        return [points[i] for (j,i) in heap]
