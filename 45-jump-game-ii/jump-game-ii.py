class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0 
        ans  = 0
        gas  = nums[0] 
        max_pos = nums[0]
        max_idx = 0
        idx = 0
        for n in nums[1:]:
            if gas == 0:
                gas = nums[max_idx] - (idx - max_idx)
                ans += 1
            idx += 1
            gas -= 1
            pos = idx + nums[idx]
            if pos >= max_pos:
                max_pos = pos
                max_idx = idx
   
        return ans + 1