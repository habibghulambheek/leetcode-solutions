class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_c  = dict()
        for i in range(len(nums)):
            idx = nums_c.get(target - nums[i],-1)
            if idx != -1:
                return [idx,i]
            nums_c[nums[i]] = i

        