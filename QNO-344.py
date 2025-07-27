class Solution(object):
    def reverseString(self, s):
      # Approach - 1
      s.reverse()

      # Approach - 2
      a ,b = 0,len(a)-1
      while a<b:
         s[a],s[b]= s[b],s[a]
         a+=1
         b-=1