s = input("String1:")
t = input("String2:")
def replaceCharactersWithUnderscores(s, t):
    result = ""

    for c in s:
        if c in t:
            result += "_"
        else:
            result += c
    return result

print(replaceCharactersWithUnderscores(s,t))