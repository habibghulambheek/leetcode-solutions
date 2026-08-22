class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        n = len(nums)
        for x in nums:
            ans ^= x
        for x in range(n+1):
            ans ^= x
        return ans