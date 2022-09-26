# Complete the code to make the HiLo game...

import random

def main():
    # Pick a random number between 1 and 100, inclusive
    secret = int(random.randrange(1, 101))
    print(secret)
    print("Can you guess my secret?")
    # put your code here
    x = -50
    i = 0
    while x != secret:

        x = int(input('Qual o numero: '))
        
        if x == secret:
            print('Sucesso')
        elif x > secret:
            print('Demasiado alto')
        else:
            print('Demasiado baixo')

        i += 1

    print('Programa terminado')

main()
