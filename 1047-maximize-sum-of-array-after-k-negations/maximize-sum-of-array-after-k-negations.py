class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        # print(nums)
        for i in range(n):
            if k <= 0:
                break
            if nums[i] < 0:
                # print("1")
                nums[i] = -nums[i]
                k -= 1
            elif nums[i] == 0:
                k = 0
            else:
                idx = i
                if i != 0:
                    if nums[i] > nums[i-1]:
                        idx -= 1
                # print("Here", k % 2)
                if k % 2 == 0:
                    k = 0

                    continue
                k = 0
    
                # print("changed" )
                nums[idx] = -nums[idx]
        idx = 1
        if k > 0:
            # k -= 1
            if k % 2 != 0:
                nums[-idx] = -nums[-idx]
            # idx += 1

        # print(nums)
        return sum(nums)