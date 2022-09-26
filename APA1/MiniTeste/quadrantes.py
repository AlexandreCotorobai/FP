x1=int(input("x1: "))
y1=int(input("y1: "))
x2=int(input("x2: "))
y2=int(input("y2: "))

def quadrante():
    if (x1>0 and x2<0) or (y1>0 and y2<0) or (x1<0 and x2>0) or (y1<0 and y2>0):
        return "Não estão no mesmo quadrante"
    else:
        return "Estão no mesmo quadrante"

print(quadrante())