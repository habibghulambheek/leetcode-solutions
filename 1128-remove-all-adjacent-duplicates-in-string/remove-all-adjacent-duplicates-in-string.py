class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for r in s:
            if stack and stack[-1] == r:
                stack.pop()
            else:
                stack.append(r)
        
        return "".join(stack)
