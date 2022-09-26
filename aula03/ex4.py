def pol(x):
    result = x**2 + 2*x + 3
    return result

p0 = pol(0)
p1 = pol(1)
p2 = pol(2)
p11 = pol(pol(1))
print('p(0): {}\np(1): {}\np(2): {}\np(p(1)): {}'.format(p0,p1,p2,p11))