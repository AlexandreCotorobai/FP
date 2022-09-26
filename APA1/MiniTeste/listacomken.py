k=int(input("k: "))
n=int(input("n: "))

def lista(k,n):
    lst=[]
    i=0
    while i<k:
        lst.append(i)
        i+=1
    return lst*n

print(lista(k,n))