l = [1,4,6,3,9,7,3,9,2,9,1,3,4]
def positionDifferenceFirstLastLargest(arr):
   max = arr[0]
   for n in arr:
       if n > max:
           max = n

   maxes =[]
   for index in range(len(arr)):
       if arr[index] == max:
           maxes.append(index) 
   return maxes[-1] - maxes[0]

print (positionDifferenceFirstLastLargest(l))


