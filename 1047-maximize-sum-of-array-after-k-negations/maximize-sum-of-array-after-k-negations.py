class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        for i in range(n):
            if k <= 0:
                break
            if nums[i] < 0:
                 nums[i] = -nums[i]
                 k -= 1
            elif nums[i] == 0:
                k = 0
            else:
                idx = i
                if i != 0:
                    if nums[i] > nums[i-1]:
                        idx -= 1
                if k % 2 == 0:
                    k = 0

                    continue
                k = 0
    
                nums[idx] = -nums[idx]
        idx = 1
        if k > 0:
            if k % 2 != 0:
                nums[-idx] = -nums[-idx]

        return sum(nums)