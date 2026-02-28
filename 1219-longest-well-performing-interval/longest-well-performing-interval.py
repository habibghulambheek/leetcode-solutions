class Solution(object):
    def longestWPI(self, nums):
        """
        :type hours: List[int]
        :rtype: int
        """
        
        # prefix = {0:-1}
        # n = len(nums)
        # k = 0
        # ans = 0
        # # -1 , +2
        # for i in range(n):
        #     k = (k + 1) if k > 8 else (k-1)

        #     ans = max()

        n = len(nums)
        prefix = {0:0}
        running_k = 0
        ans = 0
        for i in range(n):
            if nums[i] > 8:
                running_k += 1
            else:
                running_k -= 1

            if running_k > 0:

                ans = i+ 1
            else:
                if (running_k - 1) in prefix:
                    ans = max(ans,i - prefix[running_k -1])
            #  6 6 9 2 -1 + 1
            # -1 -2 -1
            if running_k not in prefix:
                prefix[running_k] = i
        return ans