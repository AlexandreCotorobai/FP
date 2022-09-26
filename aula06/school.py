# Complete o programa!

# a)
def loadFile(fname, lst):
    with open(fname, 'r', encoding='UTF-8') as file:
        i = 0
        for line in file:
            lst.append((line.strip('\n').split('\t')))
        nlst = []
        for i in range(len(lst)-1):
            if i == 0:
                nlst.append(tuple(lst[i][0:2] + lst[i][5:8]))
                # print('n')
            else:
                x = lst[i][5]
                y = lst[i][6]
                z = lst[i][7]
                # print(x,y,z)
                nlst.append(lst[i][0:2] + float(x) + float(y) + float(z))
            # nlst.append(lst[i][0:2] + float(lst[i][5]) + float(lst[i][6]) + float(lst[i][7]))
            
        print(nlst)
    
    
# b) Crie a função notaFinal aqui...
...

# c) Crie a função printPauta aqui...
...

# d)
def main():
    lst = []
    # ler os ficheiros
    loadFile("school1.csv", lst)
    # loadFile("school2.csv", lst)
    # loadFile("school3.csv", lst)
    
    # ordenar a lista
    ...
    
    # mostrar a pauta
    ...


# Call main function
if __name__ == "__main__":
    main()


