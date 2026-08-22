class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        numbers = {i:False for i in range(n+1)}
        
        for x in nums:
            numbers[x] = True
        
        for x in range(n+1):
            if numbers[x] != True:
                return x
            