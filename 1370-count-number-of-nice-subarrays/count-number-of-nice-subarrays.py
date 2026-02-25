class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Sliding windows approach
        # i = 0
        # j = 0
        # n = len(nums)
        # odds = 0
        # count = 0
        # for j in range(n):
        #     if nums[j] % 2 == 1:
        #         odds += 1
        #     if odds == k:
        #         count += 1
        #     elif odds > k:
        #         while(odds > k):
        #             if nums[i] % 2 == 1:
        #                 odds -= 1
        #             i += 1
        #         while (odds == k):
        #             if nums[i] % 2 == 1:
        #                 odds -= 1
        #             count += 1
        #             i += 1
        # return count
        # Sliding windows is not working , now let's solve it using prefix sum
        prev_odds = {0:1}
        n = len(nums)
        ctr = 0
        running_odds = 0
        for i in range(n):
            if nums[i] % 2 == 1:
                running_odds += 1
                # r -k  = i
            ctr += prev_odds.get(running_odds - k,0)
            prev_odds[running_odds] = prev_odds.get(running_odds,0) + 1
        return ctr  