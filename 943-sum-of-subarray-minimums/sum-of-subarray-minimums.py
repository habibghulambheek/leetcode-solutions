class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # n =  len(arr)
        # ans = 0
        # for i in range(n):
        #     min_num = arr[i]
        #     for j in range(i, n):
        #         if min_num > arr[j]:
        #             min_num = arr[j]
        #         ans += min_num
        # ans %= (10**9 + 7)
        # return ans

        
        stack = []
        n = len(arr)
        left  = [-1]*n
        right = [-1]*n
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                idx = stack.pop()
                right[idx] = i
            stack.append(i)
        stack = []
        for i in range(n-1,-1,-1):
            while stack and arr[stack[-1]] > arr[i]:
                idx = stack.pop()
                left[idx] = i
            stack.append(i)
     
        ans = 0 
        for i in range(n):
            l_idx = left[i] 
  
            r_idx =  right[i]
            if r_idx == -1:
                r_idx = n
            l_idx = i - l_idx 
            r_idx = r_idx - i
            ans += l_idx * r_idx * arr[i]
        return ans % (10**9  + 7)
            