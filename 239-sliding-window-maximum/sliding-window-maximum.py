# from sortedcontainers import SortedList
from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # n = len(nums)
        # ans =[]
        # window  = SortedList()
        # for i in range(k):
        #     # heapq.heappush(window, nums[i])
        #     window.add(-nums[i])
        # ans.append(-window[0]) #  Pushing the root
        # i = 0
        # for j in range(k, n):
        #     # heapq.heappop(window, nums[i])
        #     # heapq.heappush(window, nums[j])
        #     window.remove(-nums[i])
        #     window.add(-nums[j])
        #     i += 1
        #     ans.append(-window[0])
        # return ans
        # n   = len(nums)
        # ans = []
        # window = deque()
        # window.appendleft(0)
        # for i in range(1,k):
        #     if nums[i] > nums[window[0]]:
        #         window.appendleft(i)
        #     else:
        #         while nums[window[-1]] < nums[i]:
        #             window.pop()
        #         window.append(i)
        # # print(window)
        # ans.append(nums[window[0]])
        # i  = 0
        # for j in range(k,n):
        #     if nums[j] > nums[window[0]]:
        #         window.appendleft(j)
        #     else:
        #         while nums[window[-1]] < nums[j]:
        #             window.pop()
        #         window.append(j)
        #     i += 1
        #     while window[0] < i:
        #         window.popleft()
            
        #     ans.append(nums[window[0]])
        # return ans
        n = len(nums)
        ans = []
        window  = deque()
        for j in range(n):
            
            while window and window[0] < j - k +1 :
                window.popleft()

            while window and nums[window[-1]] < nums[j]:
                window.pop()
            window.append(j)
            if j >= k-1:
                ans.append(nums[window[0]])
        return ans