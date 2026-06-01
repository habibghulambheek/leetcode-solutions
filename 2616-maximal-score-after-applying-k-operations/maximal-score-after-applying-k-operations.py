import heapq
import math
class Solution(object):
    def maxKelements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums_temp = [-x for x in nums]
        heapq.heapify(nums_temp)
        score = 0
        while k > 0 :
            num =  -heapq.heappop(nums_temp)
            if num != 1:
                score += num
                # print(num, score)
                heapq.heappush(nums_temp, -math.ceil(float(num) / 3))
                k -= 1
            else:
                score += num * k
                k = 0
        return int(score)