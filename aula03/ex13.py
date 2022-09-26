n = input('number?').split(' ')
x = int(n[0])
y = int(n[1])


def mdc(a,b):
    r = a%b
    if r == 0:
        return b
    elif r > 0:
        return mdc(b, r)


print('mmc: ',mdc(x,y))
