class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort(reverse = True)
        s.sort(reverse = True)

        n = len(g)
        m = len(s)
        i = 0 
        j  = 0
        ans = 0
        while i < n and j < m:
            # print(g[i], s[j])
            if g[i] <= s[j]:
                ans += 1
                j += 1
            i += 1
        return ans

