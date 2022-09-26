k = int(input("K:"))
n = int(input("N:"))

def list(k,n):
    lst=[]
    for i in range(0,k):
        lst.append(i)
    return lst*n
print(list(k,n))   
