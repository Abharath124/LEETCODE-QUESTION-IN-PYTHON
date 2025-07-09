class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = set(nums)
        l = 0

        for i in num:
            if i-1 not in num:
                curr = i
                s = 1

                while curr+1 in num:
                    curr+=1
                    s+=1

                l = max(l,s)

        return l