class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        i = 0
        n  = len(s)
        window ={}
        # voilations = 0
        ans = 0
        # max_char = ""
        max_freq = 0
        for j in range(n):
            # print("Next iter this is")
            if not window:
                window[s[j]] = 1
            elif s[j] not in window:
                window[s[j]] = 1
            else:
                window[s[j]] += 1
            max_freq = max(max_freq, window[s[j]])
            if (j - i + 1) - max_freq > k:
                window[s[i]] -= 1
                i += 1
            ans = max(ans, j - i + 1)
            # if not window:
            #     window[s[j]] = 1
            #     max_char = s[j]
            # elif s[j] not in window:
            #     window[s[j]] = 1
            # else:
            #     window[s[j]] += 1
            #     if  window[s[j]] > window[max_char]:
            #         max_char = s[j]
            # print("Before Loop:", window, ((j - i+1) - window[max_char]))
            # while (max_char != "") and ((j - i+1) - window[max_char]) > k:
            #     # print("In this loop")             
            #     window[s[i]] -= 1
            #     if s[i] == max_char:
            #         for key in window:
            #             if window[key] > window[max_char]:
            #                 max_char = key
            #     if window[s[i]] == 0:
            #         window.pop(s[i])            
            #     i += 1   
                
            # ans = max(ans , j - i + 1)
            # print("After Loop:", window, ((j - i+1) - window[max_char]))
            # print(window,((j - i+1) - window[max_char]), max_char,((j - i+1) - window[max_char]) > k,k,(max_char != "") and ((j - i+1) - window[max_char]) > k)
        return ans
                