class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        def is_palindrome(x):
            return x if x == x[::-1] else None
        for word in words:
            ans = is_palindrome(word)
            if ans != None:
                return ans
        return ""
        