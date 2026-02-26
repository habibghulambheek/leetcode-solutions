class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix = {0:0}
        n = len(nums)
        ctr = 0
        running_sum = 0
        for j in range(n):
            running_sum += nums[j]
            r_j = running_sum % k
            ctr += prefix.get(r_j, 0)
            if r_j ==0:
                ctr += 1
            prefix[r_j] = prefix.get(r_j,0) + 1
        return ctr