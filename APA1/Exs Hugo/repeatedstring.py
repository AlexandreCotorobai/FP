
# Given a string s and an integer n, return a string 
# in which each of the characters in s is repeated n times.


def repeatCharacters(s, n):
   st = ""
   for i in s:
       st = st + i*n
   return st
