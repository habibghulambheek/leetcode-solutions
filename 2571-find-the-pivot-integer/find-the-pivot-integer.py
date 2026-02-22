class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        def prefix(s):
            return (s*(s + 1))//2
        # prefix = [0] * (n)
        # prefix[0] = 1
        # for i in range(1,n):
        #     prefix[i] = prefix[i - 1] + (i + 1)
        # print(prefix)
        # left = 0
        # [1, 3, 6, 10]
        # 3 ==  4
        left = 0
        right = prefix(n) - prefix(1)
        for i in range(n):
            if left == right:
                return (i+1)
            left  =  prefix(i+1)
            if i != (n -1):
                right =  prefix(n) - prefix(i+2)
            else:
                right == 0
        return -1