class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None
        """
        i = m - 1  # Last valid element in nums1
        j = n - 1  # Last element in nums2
        k = m + n - 1  # End of nums1 array

        # Start filling from the back
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If nums2 has leftover elements
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
