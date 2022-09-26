
# On a chessboard, positions are marked with letters between a and h for the column and a
# number between 1 and 8 for the row. The first place on the board, a1, is black. The next
# is white, alternating across a row. Odd rows start with black, even rows start with white.

# Give a 2 character input string with a letter (a-h) and a number (1-8), print "Black" or
# "White" indicating if the square is black or white.

inputStr = 'a1' 

letra = inputStr[0]
numero = int(inputStr[1])

if letra == "a" or letra == "c" or letra == "e" or letra == "g":
   if numero%2 == 0:
      print("White")
   else:
      print("Black")
else:
   if numero%2 == 0:
      print("Black")
   else:
      print("White")