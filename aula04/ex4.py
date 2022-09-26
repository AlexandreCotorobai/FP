

def factorial(n):
   assert isinstance(n, int), "n should be an int"
   assert n >= 0            , "n should not be negative"
   # Complete aqui
   r = 1
      
   while n > 0:
      r = r * n
      n -= 1
   return r