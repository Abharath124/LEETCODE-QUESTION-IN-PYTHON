class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sumdict = {0:1}
        n = len(nums)
        c = 0
        s = 0

        for i in nums:
            s += i
            if s-k in sumdict:
                c+=sumdict[s-k]
            if s in sumdict:
                sumdict[s]+=1
            else:
                sumdict[s]=1
        return c

        