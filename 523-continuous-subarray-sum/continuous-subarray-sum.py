from collections import defaultdict
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = defaultdict(int)
        if len(nums) < 2:
            return False
        prefix[0] = 1
        j = 0
        running_sum = nums[0] 
        pre_sum = 0
        for i in range(1,len(nums)):
            running_sum += nums[i]
            if running_sum%k in prefix:
                return True
            pre_sum += nums[j]
            prefix[pre_sum%k] += 1
            j += 1


        return False
            