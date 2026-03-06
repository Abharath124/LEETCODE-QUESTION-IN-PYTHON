def armstrong(n):
      # n = int(input()
      temp = n
      digit = len(str(n))
      sum_val = 0

      while temp>0:
            digit =  temp%10
            sum_val += digit**digit
            temp = temp//10

      if sum_val == n:
            print("Armstrong")           
      else:
            print("Not Armstrong")
n=int(input())
armstrong(n)
