t = [['coal', 30], ['rice', 50], ['iron', 5], ['rice', 42], ['coal', 45]]

M, Q = 0, 1

###Primeira Parte
# m = "coal"
# def cargoQuantity(t,m):
#     #Quantidade total de mercadoria do tipo m no comboio t.
#     val = 0
#     for i in t:
#         if i[M] == m:
#             val += i[Q]
#     print(val)

# cargoQuantity(t,m)


###Segunda parte
def unload(t,m,q):
    # Descarrega a quantidade q de merdadoria de tipo m
    for vagao in range(0, len(t), -1):
        print(vagao)


def main():
    t = eval(input())

    print('t:', t)
    q = unload(t, 'rice', 40)
    print("unload(t, 'rice', 40) ->", q)
    print('t:', t)
    q = unload(t, 'coal', 50)
    print("unload(t, 'coal', 50) ->", q)
    print('t:', t)
    q = unload(t, 'iron', 20)
    print("unload(t, 'iron', 20) ->", q)
    print('t:', t)

if __name__ == "_main_":
    main()








# def cargoQuantidade(t,m):

#     num = 0

#     for tupl in t:

#         if tupl[0] == m:

#             num += tupl[1]

#     return num
# print(cargoQuantidade(t,'coal'))

# def merchandise(t):

#     dic = {}

#     for tupl in t:

#         if tupl[0] in dic.keys():

#             dic[tupl[0]] += tupl[1]
#         else:

#             dic[tupl[0]] = tupl[1]

#     return dic

# print(merchandise(t))

# def unload(t, m, q):

#     num = cargoQuantidade(t,m)

#     if num < q:

#         for i in range(len(t)-1,-1,-1):

#             if t[i][0] == m:

#                 t.pop(i)

#         return q-num

#     else:

#         for i in range(len(t)-1,-1,-1):

#             if t[i][0] == m:

#                 temp = t[i][1]

#                 t[i][1] -= q

#                 if t[i][1] <= 0:

#                     q -= temp

#                     t.pop(i)

#                 else:

#                     break

#         return cargoQuantidade(t,m)

# print(t)

# print(unload(t,'rice',40))

# print(t)

# print(unload(t,'coal',50))

# print(t)

# print(unload(t,'iron',20))

# print(t)


# def main():


#     print('t:', t)
#     q = unload(t, 'rice', 40)
#     print("unload(t, 'rice', 40) ->", q)
#     print('t:', t)
#     q = unload(t, 'coal', 50)
#     print("unload(t, 'coal', 50) ->", q)
#     print('t:', t)
#     q = unload(t, 'iron', 20)
#     print("unload(t, 'iron', 20) ->", q)
#     print('t:', t)

# if __name__ == "_main_":
#     main()