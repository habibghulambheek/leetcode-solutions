class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """

        if len(num) ==  k:
            return "0"
        stack = []

        for ch in num:
            while stack and stack[-1] > ch and k > 0:
                stack.pop()
                k -= 1
            stack.append(ch)
        # if k != 0:
        while k != 0:
            stack.pop()
            k -=1
        word = "".join(stack).lstrip("0")
        return "0" if word == "" else word