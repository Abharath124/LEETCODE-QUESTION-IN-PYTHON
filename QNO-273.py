class Solution(object):
    def numberToWords(self, num):
        if num == 0:
            return "Zero"
        
        b_20 = [
            "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
            "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"
        ]

        t_10 = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        t_1000 = ["", "Thousand", "Million", "Billion"]

        def helper(n):
            if n == 0:
                return ""
            elif n < 20:
                return b_20[n - 1] + " "
            elif n < 100:
                return t_10[n // 10] + " " + helper(n % 10)
            else:
                return b_20[n // 100 - 1] + " Hundred " + helper(n % 100)

        res = ""
        i = 0
        while num > 0:
            if num % 1000 != 0:
                res = helper(num % 1000) + t_1000[i] + " " + res
            num //= 1000
            i += 1

        return res.strip()

