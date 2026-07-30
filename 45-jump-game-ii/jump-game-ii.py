class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jumps = 0
        current_end = 0 
        farthest = 0
        for i in range(len(nums) - 1 ):
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                current_end = farthest
                jumps += 1
        return jumps