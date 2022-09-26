
# On a chessboard, positions are marked with letters between a and h for the column and a
# number between 1 and 8 for the row. 

# Give a 2 character input string with a letter (a-h) and a number (1-8), print "Corner" if the 
# value indicates a square on a corner. Print "Border" if the value indicates a square on an 
# edge of the board. Otherwise, print "Inside".

inputStr = 'a1' 

letra = inputStr[0]
numero = int(inputStr[1])

if letra == 'a' or letra == 'h':
    if numero == 1 or numero == 8:
        print('Corner')
    else:
        print('Border')
elif numero == 1 or numero == 8:
    print('Border')
else:
    print('Inside')