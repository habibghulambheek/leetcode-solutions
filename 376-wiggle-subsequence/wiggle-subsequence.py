class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # ans = 0
        # n = len(nums)
        # if n == 1:
        #     return n
        # prev_sign  =  nums[1] - nums[0]
        # ans = 1
        # if prev_sign != 0:
        #     prev_sign /= abs(prev_sign)
        #     ans = 2

        # i = 1
        # for j in range(2,n):
        #     sign = nums[j] - nums[i]
        #     print(sign, nums[j], nums[i], j,i)
        #     if sign != 0:
        #         sign /= abs(sign)
        #     if sign != 0 and sign != prev_sign:
        #         prev_sign = sign
        #         ans += 1
        #         i = j
        # return ans
        n  = len(nums)
        count  = 1
        if n == 1:
            return count

        # [1,7,4,9,2,5]
        # count = 1
        # p_sign = 
        # c_sign = 
        # i 
        prev_diff = nums[1] - nums[0]
        prev_sign = 0
        if prev_diff != 0:
            prev_sign = prev_diff / abs(prev_diff)
            count += 1
    
        for i in range(2,n):
            curr_diff =  nums[i] - nums[i-1]
            curr_sign = 0
            if curr_diff != 0:
                curr_sign = curr_diff / abs(curr_diff)
            if curr_sign != 0 and curr_sign != prev_sign:
                count += 1
                prev_sign = curr_sign
        return count