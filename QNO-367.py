class Solution(object):
    def isPerfectSquare(self, num):
        if num < 0:
            return False
        r = int(math.sqrt(num))
        return r*r == num