class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def binary_search(start, end):
            if start > end:
                return -1
            mid = start + (end - start)//2
            if nums[mid] ==  target:
                return mid 
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
            return binary_search(start, end)
        return binary_search(0, len(nums)-1)
            
        