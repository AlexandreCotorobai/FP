n = int(input("n?"))

def factorial(n):
   assert n>=0
   res = n
   while n > 1 :
      res = res * (n-1)
      n = n - 1
   return res

print(factorial(n))

   

