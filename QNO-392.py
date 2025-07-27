class Solution(object):
    def isSubsequence(self, s, t):
      i = 0
      for j in t:
            if i < len(s) and s[i]==j:
                i+=1
      return i ==len(s) 