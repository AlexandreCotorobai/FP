from typing import Collection


target = float(input("Target:"))
x = float(input("Numero 1:"))
y = float(input("Numero 2:"))

def closertoTarget(x,y,target):
    if abs(x-target) > abs(y-target):
        return y
    elif abs(x-target) < abs(y-target):
        return x
    else:
        if x < y:
            return x
        else:
            return y


print(closertoTarget(x,y,target))