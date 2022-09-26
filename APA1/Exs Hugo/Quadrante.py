x1 = float(input("x1:"))
y1 = float(input("y1:"))
x2 = float(input("x2:"))
y2 = float(input("y2:"))

def quadrante():
    if ((x1<0 and x2>0) or (x1>0 and x2<0) or (y1<0 and y2>0) or (y1>0 and y2<0)):
        return "Não estão no mesmo quadrante"
    else:
        return "Estão no mesmo quandrante"


print(quadrante())
