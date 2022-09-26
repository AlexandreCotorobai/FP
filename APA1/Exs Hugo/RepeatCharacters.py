s = input("String:")
n = int(input("Number of times:"))

def repeaCharacters (s,n):
    p = ""
    for i in s:
        p += i*n
    return p 




print (repeaCharacters(s,n))

#def repeatCharacters(s, n):
#    return ''.join([c * n for c in s])