class Solution(object):
    def groupAnagrams(self, strs):
      ana = defaultdict(list)
      for i in  strs:
            key = tuple(sorted(i))
            ana[key].append(i)
      return list(ana.values())