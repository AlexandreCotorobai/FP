s=input("string:")
n=int(input("número:"))

def repeatCharacters(s,n):
    string=""
    for letra in s:
        string+=letra*n
    return string

print(repeatCharacters(s,n))