# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """
#
#    def length(self):
#        """
#        :rtype int
#        """

class Solution(object):
    def findInMountainArray(self, target, mountainArr):
        """
        :type target: integer
        :type mountain_arr: MountainArray
        :rtype: integer
        """
        # Step 1: Find the peak index
        def peak():
            l,r = 0,mountainArr.length()-1

            while l<r:
                m = (l+r) // 2
                if mountainArr.get(m) < mountainArr.get(m+1):
                    l=m+1
                else:
                    r=m
            return l # Peak Index
            
        # Step 2: Binary Search in Increasing order
        def BSI(l,r):  #Binary Search Increasing
            while l<=r:
                m = (l+r)//2
                val =mountainArr.get(m)
                if val == target:
                    return m
                elif val<target:
                    l=m+1
                else:
                    r=m-1
            return -1

        # Step 3: Binary Search in Decreasing order
        def BSD(l,r):
            while l<=r:
                m=(l+r)//2
                val = mountainArr.get(m)
                if val == target:
                    return m
                elif val>target:
                    l=m+1
                else:
                    r=m-1
            return -1

        p = peak()  # Find the peak index

        # Search on the increasing side
        l_r = BSI(0,p)
        if l_r != -1:
            return l_r

        # If not found, search on the decreasing side
        return BSD(p+1 , mountainArr.length() -1)
