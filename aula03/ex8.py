def intersects(a1,b1,a2,b2):
    assert a1<=b1
    assert a2<=b2

    if b1<=a2 or b2<=a1:
        return False
    else:
        return True

a1, b1 = input().split(',')
a2, b2 = input().split(',')

print(intersects(a1,b1,a2,b2))