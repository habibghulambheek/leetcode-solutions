class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # i = 0
        # n =  len(s)
        # # alphabets = set()
        # max_len = 0
        # curr_len = 0
        # for j in range(n):
        #     while (s[j] in s[i:j]):
        #             i += 1
        #             curr_len -= 1
        #     curr_len += 1
        #     max_len = max(max_len, curr_len)
        # return max_len
        i = 0
        n = len(s)
        window = set()
        max_len = 0
        curr_len = 0
        for j in range(n):
            while s[j] in window:
                window.remove(s[i])
                i += 1
                curr_len -= 1
            window.add(s[j])
            curr_len += 1
            if max_len < curr_len:
                max_len = curr_len
        return max_len

