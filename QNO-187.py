class Solution(object):
    def findRepeatedDnaSequences(self, s):
      
      count = defaultdict(int)
      res = []

      for i in range(len(s)-9):
            sub = s[i:i+10]
            count[sub]+=1

            if count[sub] ==2:
                res.append(sub)

      return res