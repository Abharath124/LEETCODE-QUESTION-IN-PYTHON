def prime(n):
      if n<=1:
            return "its not prime"
      else:
            for i in range(2,int(n*0.5)+1):
                  if n%i == 0:
                        return "not prime"
                        break
            else:
                  return "prime"
            
n = int(int(input()))
print(prime(n))
