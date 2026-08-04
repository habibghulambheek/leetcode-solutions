class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        
        last_idx = {c:i for i, c in enumerate(s)}
        n = len(s)

        ans = []
        start, end = 0, last_idx[s[0]]
        for i in range(n):
            end = max(end,last_idx[s[i]])
            if i >= end:
                ans.append(end - start + 1)
                start = i + 1
            
        return ans