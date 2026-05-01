class Solution(object):
    def mostCompetitive(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        stack  = []
        # [84,10,71,23,66,61,62,64,34,41,80,25,91,43,4,75,65,13,37,41,46,90,55,8,85,61,95,71]
        n = len(nums) 
        remove = n - k
        for i in range(n):
            # print("Req elements:",(k - len(stack)) ,"Left:", n - (i), "Stack:", stack)
               
            while stack and stack[-1] > nums[i] and remove > 0:
                    stack.pop()
                    remove -= 1
            # print("After popping by ", nums[i] ,":", stack)
       
            stack.append(nums[i])
            # print("After appending:", stack)
            
        return stack[0:k]