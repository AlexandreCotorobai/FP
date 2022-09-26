arr=[2,3,1,4,7,1]
n=5

def returnConsecutiveAverage(arr, n):
    res = [sum(arr[0:n]) / n]
    somatorio = n
    contador = 0
    while somatorio != len(arr):
        somatorio += 1
        contador += 1
        res += [sum(arr[contador:somatorio]) / n]
    return res

print(returnConsecutiveAverage(arr,n))