class Solution(object):
    def plusOne(self, digits):
        
      n = len(digits)

      for i in digits:
            n = n*10+i
      n+=1
      return [int(x) for x in str(n)]