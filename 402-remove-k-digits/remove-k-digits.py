class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if len(num) <=  1 and k > 0:
            return "0"
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
        non_zero = False
        word = ""
        for s in stack:
            if s == "0":
                if non_zero == True :
                    word += s
            else:
                word += s
                non_zero =True
        return "0" if word == "" else word