class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        closing_set = {")":"(","}":"{","]":"["}
        stack = []

        for char in s:
            if char in closing_set:
                if stack:
                    if closing_set[char] != stack.pop():
                        return False
                else:
                    return False
            else:
                stack.append(char)
        if stack:
            return False
        return True