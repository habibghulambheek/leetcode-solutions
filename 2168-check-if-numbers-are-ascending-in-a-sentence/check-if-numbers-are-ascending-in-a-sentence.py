class Solution(object):
    def areNumbersAscending(self, s):
        """
        :type s: str
        :rtype: bool
        """
        prev = 0
        for word in s.split():
            if word.isnumeric():
                current = int(word)
                if prev >= current:
                        return False
                prev = current
        return True