from collections import Counter
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

        task_count  = Counter(tasks).values()

        min_heap  = []
        task_heap = [-x for x in task_count]
        heapq.heapify(task_heap)

        time = 0
        while task_heap or min_heap:
            time += 1

            while min_heap and time > min_heap[0][0]:
                heapq.heappush(task_heap, -heapq.heappop(min_heap)[1])

            if task_heap:
                new_ctr = -heapq.heappop(task_heap) - 1
                if new_ctr > 0:
                    heapq.heappush(min_heap,(time + n , new_ctr))
        return time