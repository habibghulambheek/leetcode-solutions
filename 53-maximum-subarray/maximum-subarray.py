class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        subarray_sum = nums[0]
        n = len(nums)
        running_sum  = nums[0]
        for i in range(1,n):
            if running_sum < 0:
                running_sum = nums[i]
            else:
                running_sum += nums[i]
            subarray_sum  = max(running_sum, subarray_sum)
        return subarray_sum