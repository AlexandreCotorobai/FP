s = input("String: ")

def longestPrefixRepeated(s):
    p = s[:len(s)//2]
    while len(p)>0:
        if p in s[len(p):]:
            return p
        else:
            p=p[:len(p)-1]
    return p
  
print(longestPrefixRepeated(s))        

#________________________________________

def longestPrefixRepeated(s):
    i=0
    prefixoEscolhido=""

    while (i+1 <= len(s) - (i+1)):
        prefixoSelecionado=s[0:(i+1)]
        if prefixoSelecionado in s[(i+1):]:
            prefixoEscolhido=prefixoSelecionado
        i+=1
    return prefixoEscolhido
    