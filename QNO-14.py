class Solution(object):
    def longestCommonPrefix(self, strs):
        
      if not strs:
            return ""
      pre = strs[0]

      for i in range(strs[1:]):
          while not i.startswith(pre):
              pre=pre[:-1]
              if not pre:
                  return ""
      return pre
      