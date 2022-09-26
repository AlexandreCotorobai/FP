# feito por mim, mal feito
# with open('names.txt', 'r') as doc:
#     for line in doc:
#         apelidos = {}
#         nomes = line.split(' ')
#         ultimoindex = len(nomes)-1
#         if nomes[ultimoindex][0:-1] not in apelidos:
#             apelidos[nomes[ultimoindex][0:-1]] = nomes[0]
#         else:
#             apelidos[nomes[ultimoindex][0:-1]].add(nomes[0])
#         print(apelidos)


d = {}
with open("names.txt") as f:
    for line in f:
        names = line.strip().split()
        first,last = names[0],names[-1]
        
        if last not in d:
            d[last] = set()
        d[last].add(first)

for last in d:
    print(last, ":", d[last])