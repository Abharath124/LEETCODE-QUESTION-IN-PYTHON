class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def sqsum(num):
            res = 0
            while num > 0:
                r = num%10
                res = res+r*r
                num = num // 10
            return res
        seen = set()
        while sqsum(n) not in seen:
            sum1 = sqsum(n)
            if  sum1 == 1:
                return True
            else:
                seen.add(sum1)
                n=sum1
        return False
        