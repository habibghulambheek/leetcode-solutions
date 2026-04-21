class Solution(object):
    def removeKdigits(self, num, k):
        if len(num) == k:
            return "0"

        stack = []

        for ch in num:
            while stack and stack[-1] > ch and k > 0:
                stack.pop()
                k -= 1
            stack.append(ch)

        while k > 0:
            stack.pop()
            k -= 1

        result = "".join(stack).lstrip("0")
        return result if result else "0"