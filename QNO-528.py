import random

class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.accw = []
        temp = 0
        for v in w:
            temp += v
            self.accw.append(temp)
        self.ttl = self.accw[-1]

    def pickIndex(self):
        """
        :rtype: int
        """
        rnd = random.random() * self.ttl
        for i, v in enumerate(self.accw):
            if rnd < v:
                return i