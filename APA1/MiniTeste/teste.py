def reapeatNumTimes(n):
   lst=[]
   i=1
   while i<=n:
      lst.append(i)*i
      i+=1
   return lst

print(reapeatNumTimes(4))