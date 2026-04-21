class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        star =  "*"
        stack = []
        for ch in s:
            # print("before:", stack)
            if stack and ch == star:
                stack.pop()
            else:
                stack.append(ch)
            # print("After:", stack)
            
        return "".join(stack)