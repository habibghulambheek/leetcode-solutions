class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        n = len(s)
        # "cbaacabcaaccaacababa"
        #  0,
        last = {c: i for i, c in enumerate(s)}
        # print(last)
        elements = set()
        for i in range(n):
            if s[i]  in elements:
                    continue
            while stack and s[stack[-1]] > s[i]:
                # print(stack,stack[-1],i,s[i],s[i::])

                if i < last[s[stack[-1]]] :
                    elements.discard(s[stack[-1]])
                    stack.pop()
                else:
                    break
            stack.append(i)
            elements.add(s[i])
        return "".join([s[i] for i in stack])