def longestPrefix(str):
    controlSuffix = len(str)//2 # variável para controlar o tamanho do sufixo
    prefix = str[:len(str)//2] # vou assumir que o prefixo começa pelo mais longo, sendo este metade da palavra
    suffix = str[controlSuffix:] # dividi a palavra em 2 partes: o prefixo e o sufixo
    while len(prefix) > 1: # o tamanho do prefixo é maior que 1, nao incluindo 1
        if prefix in suffix: # se o prefixo estiver dentro do sufixo, ou seja, se repita no sufixo, será este o longestPrefix repeating, pois o prefixo neste loop será sempre o maior (longest prefix repeating)
            return prefix 
        prefix = prefix[:-1] # se não estiver dentro, diminuir o tamanho do prefixo, removendo uma letra do final
        controlSuffix -= 1 # reduzir o tamanho da variável de controlo do tamanho do sufixo
        suffix = str[controlSuffix:] # o sufixo será o que vem a seguir ao prefixo, logo, tendo o prefixo diminuido na linha 8, o sufixo aumentará
    return ("No repeating prefix") # se não houver prefixo repetente, será devolvida uma string a dizer "No repeating prefix"


# TESTES #

string = "olasouumtesolte"
string1 = "abacoawgojsdkhjawi4yujasdhkabac"
string2 = "abcdefghijklma"
print(longestPrefix(string))
print(longestPrefix(string1))
print(longestPrefix(string2))