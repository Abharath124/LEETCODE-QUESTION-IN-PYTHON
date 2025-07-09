class Solution(object):
    def maxProduct(self, nums):

      if not nums:
            return 0
      
      pre = 1
      suf = 1
      n = len(nums)
      res = nums[0]


      for i in range(n):
          pre *=nums[i]
          suf *=nums[n-i-1]   
          res = max(res,pre,suf)

      return res