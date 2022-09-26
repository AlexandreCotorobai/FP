
def primesUpTo(n):
    u = range(2,n+1)
    pp = set(u)
    p = 2

    while p**2 <= n:
        if p in pp:
            pp -= set(range(p**2, n+1, p))
        p += 1
    
    return pp

def main():
    # Testing:
    s = primesUpTo(1000)
    print(s)

    # Do some checks:
    assert primesUpTo(30) == {2,3,5,7,11,13,17,19,23,29}
    assert len(primesUpTo(1000)) == 168
    assert len(primesUpTo(7918)) == 999
    assert len(primesUpTo(7919)) == 1000
    print("All tests passed!")

if __name__ == "__main__":
    main()

