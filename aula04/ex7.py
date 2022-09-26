i = 0

coisas = []

while True:
    num = input('Numero? ')
    if num == '':
        break
    else:
        coisas.append(float(num))

    i += 1

def average(x):
    return sum(x) / len(x)


print('Valor medio', average(coisas))