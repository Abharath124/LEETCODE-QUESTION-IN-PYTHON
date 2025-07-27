class Solution(object):
    def sortArrayByParityII(self, nums):
        res = [0]*len(nums)
        even = odd = 0, 1

        for i in nums:
            if i %2 ==0:
                res[even] == i
                even+=2
            else:
                res[odd] == i
                odd+=2
        return res