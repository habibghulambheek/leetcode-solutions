class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        prefix  = [0] * n 
        prefix[0] = nums[0]

        for i in range(1,n):
            prefix[i] = prefix[i - 1] + nums[i]

        # print(prefix)

        left = 0
        right = prefix[n-1] - prefix[0]

        for i in range(n):
            if left == right:
                return i
            left = prefix[i]
            if i != n -1:
                right = prefix[n -1] - prefix[i+1]
            else:
                right = 0
        return -1