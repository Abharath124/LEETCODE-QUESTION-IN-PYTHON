class Solution(object):
    def finalValueAfterOperations(self, operations):
      c=0
      for i in operations:
            if i == "X++" or i=="++X":
                c+=1
            elif i == "X--" or i=="--X":
                c-=1
      return c