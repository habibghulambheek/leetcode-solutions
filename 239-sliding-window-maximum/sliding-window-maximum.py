from sortedcontainers import SortedList
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        ans =[]
        window  = SortedList()
        for i in range(k):
            # heapq.heappush(window, nums[i])
            window.add(-nums[i])
        ans.append(-window[0]) #  Pushing the root
        i = 0
        for j in range(k, n):
            # heapq.heappop(window, nums[i])
            # heapq.heappush(window, nums[j])
            window.remove(-nums[i])
            window.add(-nums[j])
            i += 1
            ans.append(-window[0])
        return ans
