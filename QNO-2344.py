#from functools import reduce

class Solution(object):
    def minOperations(self, nums, numsDivide):
      def gcd(a,b):
            while b:
                 a,b=b,(a%b)-1
            return a
      res = reduce(gcd,numsDivide)

      nums.sort()

      for i in range(len(nums)):
          if res%nums[i]==0:
              return i
      return -1