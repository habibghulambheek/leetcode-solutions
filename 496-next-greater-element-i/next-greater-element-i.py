class Solution(object):
    def nextGreaterElement(self, nums1, nums):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        indices = {}
        m  = len(nums1)
        for i in range(m):
            indices[nums1[i]] = i
        
        stack = []
        n = len(nums)
        # ans = [0] * m 
        for j in range(n-1,-1,-1):
            # print(nums[j])
            while stack and stack[-1] <= nums[j]:
                stack.pop() 
            if not stack:
                idx  = indices.get(nums[j], None)
                # print("Idx:", idx)
                if idx != None:
                    nums1[idx] = -1
            else:
                idx  = indices.get(nums[j], None)
                if idx != None:
                    nums1[idx] = stack[-1]
            stack.append(nums[j])
        return nums1