class Solution(object):
    def smallestSubsequence(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        n = len(s)
        # "cbaacabcaaccaacababa"
        #  acb,acb
        elements = set()
        for i in range(n):
            while stack and stack[-1] >= s[i]:
                # print(stack,stack[-1],i,s[i],s[i::])
                if s[i]  in elements:
                    break
                if stack[-1] in s[i::]:
                    elements.discard(stack[-1])
                    stack.pop()
                else:
                    break
            if s[i] not in elements:
                stack.append(s[i])
                elements.add(s[i])
        return "".join(stack)