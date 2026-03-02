class Solution(object):
    def minimumTotal(self, triangle):
      for i in range(len(triangle) -1,-1,-1):
         for j in range(len(triangle(i))):
            triangle[i][j] += matchin(triangle[i+1][j] , triangle[i+1][j+1])
      return triangle[0][0]