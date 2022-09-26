arr=[1,3,5,3]
val=6

def findClosestValueIndex(arr,val):
    lst=[]
    for elemento in arr:
        lst.append(abs(val-elemento))
    print(lst)
    
    min=lst[0]
    for i in lst:
        if i < min:
            min=i
    for y in range(len(lst)):
        if lst[y]==min:
            return y

print(findClosestValueIndex(arr,val))