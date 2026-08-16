from collections import Counter, defaultdict
import math
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts =  Counter(nums)
        idx_dict = defaultdict(list)

        n = len(nums) 

        for i in range(n):
            value = idx_dict.get(nums[i], [-1,-1])
            if value == [-1,-1]:
                idx_dict[nums[i]] = [i,i]
            else:
                value[1] = i
                idx_dict[nums[i]] = value
        # print(counts, idx_dict)
        max_degree = max(counts.values())
        ans = 99999999999999
        for x in nums:
            if counts[x] == max_degree:
                ans = min(idx_dict[x][1] - idx_dict[x][0] + 1 , ans)
        return ans