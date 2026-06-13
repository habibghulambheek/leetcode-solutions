class Solution(object):
    def maximumProduct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heapq.heapify(nums)
        # print(k)
        while k != 0:
            heapq.heapreplace(nums, nums[0]+1)
            k -= 1
        result= 1
        while len(nums)>0:
            x= heapq.heappop(nums)
            result =(result*x )% (10**9+7)
        return result