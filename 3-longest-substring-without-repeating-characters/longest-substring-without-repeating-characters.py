class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        window = set()
        i = 0 
        n = len(s)
        max_len = 0
        for j in range(n):
            while s[j] in window:
                window.remove(s[i])
                i+= 1
            window.add(s[j])
            max_len = max(j-i+1, max_len)
        return max_len