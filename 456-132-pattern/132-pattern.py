class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        stack = []
        mid  = None
        n = len(nums)
        for i in range(n-1,-1,-1):
            while stack and stack[-1] < nums[i]:
                value = stack.pop()
                mid = value
            if mid != None and mid > nums[i]:
                return True
            stack.append(nums[i])
        return False