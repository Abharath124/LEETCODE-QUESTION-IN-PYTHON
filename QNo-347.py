class Solution(object):
    def topKFrequent(self, nums, k):
        
        freq = Counter(nums)

        res = freq.most_commn(k)
        return [item[0] for item in res]