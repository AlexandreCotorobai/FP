a=[2,-3,5,1]

def soma(a):
    lst=[]
    for elemento in a:
        if elemento >= 0:
            lst.append(elemento)
        else:
            if (sum(lst)+elemento)==0:
                lst.append(elemento)
    return sum(lst)

print(soma(a))