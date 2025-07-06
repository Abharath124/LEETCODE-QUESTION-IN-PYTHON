class Solution(object):
    def minSubArrayLen(self, target, nums):
        
        l = 0
        t = 0
        n = len(nums)
        min_len = float('inf')


        for r in nums:
            t+=nums[r]

            while t>=target:
                min_len = min(min_len,l-r+1)
                t-=nums[l]
                l+=1