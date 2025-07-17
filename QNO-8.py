class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """

        s = s.strip()

        if(len(s) == 0):
            return 0

        nums = []

        negative = 1


        for i in range(len(s)):
            if(i == 0):
                if(s[i] == "-"):
                    negative = -1
                    continue
                if(s[i] == "+"):
                    negative = 1
                    continue

            if(s[i].isnumeric()):
                nums.append(int(s[i]))
            else:
                break
                
        value = 0
        mult = 1

        nums = nums[::-1]
        for num in nums:
            value = value + num * mult
            mult = mult * 10
        
        value = value * negative

        if (value < (-2) ** 31):
            return (-2) ** 31
        if (value > (2 ** 31) - 1):
            return (2 ** 31) - 1

        return value
        