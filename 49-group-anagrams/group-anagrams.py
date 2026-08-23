class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = {}
        for x in strs:
            key = "".join(sorted(x))
            groups[key] = groups.get(key,[])
            groups[key].append(x)
        ans  = []
        for key, value in groups.items():
            ans.append(value)
        return ans