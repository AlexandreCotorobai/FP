lst=[2,3,5,3,2,5,1]

def positionDifferenceFirstLastLargest(lst):
    contador = -1
    maior=lst[0]
    l=[]
    for numero in lst:
        if maior < numero:
            maior=numero 
    for elemento in lst:
        contador += 1
        if elemento==maior:
            l += [contador]
    return l[0]-l[-1]

print(positionDifferenceFirstLastLargest(lst))


#___________________________________________________

lst = [1, 4, 6, 3, 4, 7, 5, 7]

def positionDifferenceFirstLastLargest(lst):
    max = lst[0]
    for n in lst:
        if n > max :
            max = n

    maxes = []
    for i in range(len(lst)):
        if lst[i] == max:
            maxes.append(i)
    return maxes[0] - maxes[-1]

print(positionDifferenceFirstLastLargest(lst))