# Given a string s and a string t, return a string in which all the characters 
# of s that occur in t have been replaced by a  sign. The comparisons are 
# case sensitive.
s="Hello"
t="Hii"


def replaceCharactersWithUnderscores(s, t):
    str=""
    for elemento in s:
        if elemento in t:
            str+="_"
        else:
            str+=elemento
    return str

print(replaceCharactersWithUnderscores(s,t))