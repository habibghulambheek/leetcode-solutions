class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix = {0:1}
        # n = len(nums)
        ctr = 0
        running_sum = 0
        for num in nums:
            running_sum += num
            r_j = running_sum % k
            ctr += prefix.get(r_j, 0)
            prefix[r_j] = prefix.get(r_j,0) + 1
        return ctr