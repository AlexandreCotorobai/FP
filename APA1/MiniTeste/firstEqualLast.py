# Given a list a, return the longest n so that 
# the first n elements equal the last n elements.
a=[5,3,4,5,3]

def firstEqualLast(a):
    n=1
    while n <= len(a) // 2:
       if a[:n] == a[-n:]:
          return n
       n += 1
    return 0

print(firstEqualLast(a))

