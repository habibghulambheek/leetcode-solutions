class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def comparision_function(x,y):
            if (x + y) > (y + x):
                return -1
            elif (y + x) > (x + y):
                return 1 
            return 0
        str_nums = list(map(str,nums))
        str_nums.sort(key = cmp_to_key(comparision_function))
        ans  =  "".join(str_nums) 
        if ans[0] == "0":
            ans = "0"
        return ans


        
