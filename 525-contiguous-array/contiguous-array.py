class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n =  len(nums)
        running_balance = 0
        prefix = {}
        ans = 0
        
        for i in range(n):
            if nums[i] == 1:
                running_balance = running_balance + 1 
            else:
                running_balance = running_balance - 1 
            if running_balance == 0:
                ans  = i + 1
            elif running_balance in prefix:
                ans = max(ans,i - prefix[running_balance])
            if running_balance not in prefix:
                prefix[running_balance] = i
        return ans