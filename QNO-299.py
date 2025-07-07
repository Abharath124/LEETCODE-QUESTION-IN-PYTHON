class Solution(object):
    def getHint(self, secret, guess):
      secret_count = Counter()
      guess_count =Counter()

      bulls = 0

      for s,g in zip(secret,guess):
          if s==g:
            bulls+=1
          else:
            secret_count[s]+=1
            guess_count[g]+=1
      cows = 0
      for d in '0123456789':
          cows += min(secret_count[d] ,guess_count[d])

      return str(bulls) + 'A' + str(cows) + 'B'
