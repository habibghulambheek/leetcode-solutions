class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        
        last_idx = {}
        # start_idx = {}
        n = len(s)
        for i in range(n-1,-1,-1):
            # print(i)
            if s[i] not in last_idx:
                last_idx[s[i]] = i
        # print(last_idx)
        ans = []
        start, end = 0, last_idx[s[i]]
        for i in range(n):
            end = max(end,last_idx[s[i]])
            if i >= end:
                ans.append(end - start + 1)
                start = i + 1
            
        return ans