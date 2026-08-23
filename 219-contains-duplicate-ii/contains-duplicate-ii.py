class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        window = set()
        n = len(nums)
        for i in range(min(k+1, n)):
            if nums[i] in window:
                return True
            window.add(nums[i])
        i = 0
        for j in range(k+1,n):
            window.remove(nums[i])
            if nums[j] in window:
                return True
            window.add(nums[j])
            i += 1
        return False