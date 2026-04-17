class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        running_sum = 0
        i = 0
        n = len(nums)
        min_len = n + 1
        for j in range(n):   
            running_sum += nums[j]         
            while running_sum >= target:
                min_len = min(min_len, j - i + 1)

                running_sum -= nums[i]
                i += 1
        if min_len == n + 1:
            return 0
        return min_len