class Solution(object):
    def runningSum(self, nums):
      res = []
      t = 0
      for i in nums:
            t+=i
            res.append(t)
      return res
