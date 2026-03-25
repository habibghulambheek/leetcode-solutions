class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = [-1] * n
        stack = []
        for j in range(2):
            for i in range(n):
                while stack and nums[stack[-1]] < nums[i]:
                    idx = stack.pop()
                    ans[idx] = nums[i]
                if j == 0:
                    stack.append(i)
        
        return ans