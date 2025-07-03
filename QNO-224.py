class Solution(object):
    def calculate(self, s):
        stack = []
        res = 0
        sign = 1
        num =0

        for i in s:
            if i.isdigit():
                num = num*10+int(i)
            elif i == '+':
                res+=sign*num
                num=0
                sign=1
            elif i=='-':
                res-=sign*num
                num=0
                sign=-1
            elif i=='(':
                stack.append(res)
                stack.append(sign)
                num=0
                sign=-1

            elif i==')':
                res+=sign*num
                num=0
                res*=stack.pop()
                res+=stack.pop()
        res+=sign*num
        return res
