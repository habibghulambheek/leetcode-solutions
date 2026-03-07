class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # O(n*n), O(n)
        # brute force
        # n = len(nums)
        # ctr  = 0
        # for i in range(n):
        #     curr_set = set()
        #     curr_size = 0
        #     for j in range(i,n):
        #         if nums[j] not in curr_set:
        #             curr_set.add(nums[j])
        #             curr_size += 1
        #         if curr_size == k:
        #             ctr += 1
        #         elif curr_size > k:
        #             break
        # return ctr
        n = len(nums)
        def atMost(count):
            ctr  = 0
            i = 0 
            j = 0
            ferq = {}
            for j in range(n):
                ferq[nums[j]] = ferq.get(nums[j],0) + 1
                while len(ferq.values()) > count:
                    ferq[nums[i]] -=  1
                    if ferq[nums[i]] == 0:
                        ferq.pop(nums[i])
                    i += 1  
                ctr += j - i + 1
            return ctr
        return atMost(k) - atMost(k - 1)