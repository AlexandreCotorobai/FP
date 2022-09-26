a = [1,2,3,1,2,3]
def firstEqualLast(a):
    n = 1
    while n <= len(a) // 2:
        if a[:n] == a[-n:]:
            print(n)
            return n
        n += 1
    return 0
print(firstEqualLast(a))