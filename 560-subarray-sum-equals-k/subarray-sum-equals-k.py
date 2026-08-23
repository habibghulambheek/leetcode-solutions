from collections import defaultdict
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n =  len(nums)
        prefix =  [0 for _ in range(n)]
        prefix[0] = nums[0]
        for i in range(1,n):
            prefix[i] = prefix[i-1] + nums[i]
        
        prev_sums =  defaultdict(int)

        ans = 0 
        prev_sums[0] = 1
        for x in prefix:
            
            ans += prev_sums[x - k]
            prev_sums[x] += 1
        return ans