def max3(n1,n2,n3):
    if n1>n2:
        if n1>n3: return n1
        else: return n3
    else:
        if n2>n3: return n2
        else: return n3

n1 = int(input('n1? '))
n2 = int(input('n2? '))
n3 = int(input('n3? '))

print(max3(n1,n2,n3))