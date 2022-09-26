"""
Dada uma string, construa e devolva uma nova string onde
todas as letras 'x' apareçam movidas para o fim da string.
A função tem de ser recursiva. Não pode usar ciclos.

Given a string, return a new string where all the 
'x' chars have been moved to the end of the string.
The function must be recursive. You cannot use loops.

endX("xxre") → "rexx"
endX("xxhixx") → "hixxxx"
endX("hixhix") → "hihixx"
"""

def endX(s):
   if len(s) <= 1:
      return s
   first , rest = s[:1], s[1:]

   if first == 'x':
      return endX(rest) + 'x'
   else:
      return first + endX(rest)
      
