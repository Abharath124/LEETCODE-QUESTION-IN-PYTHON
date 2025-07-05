class Solution(object):
    def breakPalindrome(self, palindrome):

      if palindrome <= 1:
         return ""
      
      palindrome = list(palindrome)

      for i in range(len(palindrome)//2):
         if palindrome[i] != 'a':
            palindrome[i] = 'a'
            return "".join(palindrome)
         
      palindrome[i] = 'b'
      return "".join(palindrome)
                  