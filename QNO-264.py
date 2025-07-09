class Solution(object):
    def nthUglyNumber(self, n):
      
      ugly = [1]*n
      i2 = i3=i5=0

      for i in range(1,n):
            n2 = ugly[i2]*2
            n3 = ugly[i3]*3
            n5 = ugly[i5]*5

            next_ugly = min(n2,n3,n5)
            ugly[i] = next_ugly


            if next_ugly == n2:
                i2+=1
            
            if next_ugly == n3:
                i3+=1

            if next_ugly == n5:
                i5+=1
      return ugly[-1]