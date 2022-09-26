
def inputFloatList():
    lista = []

    while True:
        n = input('Numero? ')
        if n == '':
            break
        else:
            lista.append(float(n))
    return lista

def countLower(lst, v):

    count = 0

    for i in lst:
        if i < v:
            count += 1

    print('Existem', count, 'elementos inferiores a', v)

def minmax(lst):
    max = lst[0]
    min = lst[0]

    for i in lst:
        if i > max:
            max = i
        if i < min:
            min = i
    
    return min, max

def vmedio(mini, maxi):
    vmedio = (mini + maxi) / 2
    print(vmedio)

    countLower(lst, vmedio)


lst = inputFloatList()
print('LISTA: ', lst)

v = float(input('Valor de referencia? '))

countLower(lst, v)

a, b = minmax(lst)
print('min: ', a, '\nmax: ', b)

vmedio(a, b)