class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        j = 0
        n = len(nums)
        k = n
        while j < n:
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
            else:
                k -= 1
            j += 1
        return k