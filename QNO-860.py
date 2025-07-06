class Solution(object):
    def lemonadeChange(self, bills):
      f , t = 0 , 0

      for i in bills:
          if i == 5:
            f+=1
          elif i == 10:
              if f == 0:
                  return False
              f-=1
              t+=1
          elif i == 20:
                if t > 0 and f > 0:
                    t-=1
                    f-=1
                elif f>=3:
                    f-=3
                else:
                    return False
      
                
                
