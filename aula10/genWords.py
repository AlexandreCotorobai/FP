
# Generates all length-3 words with symbols taken from the given alphabet.
from inspect import trace


def genWords3(symbols):
    # return [ x+y+z for x in symbols for y in symbols for z in symbols ]
    lst = []
    for x in symbols:
        for y in symbols:
            for z in symbols:
                lst.append(x+y+z)
    return lst

# Generates all length-n words with symbols taken from the given alphabet.
def genWords(symbols, n):
    # if n > 0:
    #     return [x+y for x in symbols for y in genWords(symbols, n-1)]
    # return ['']

    if n > 0:
        return [x+y for x in symbols for y in genWords(symbols, n-1)]
    return ['']

    ## RESOLUCAO STOR
    # if n == 0:
    #     return ['']
    # lst1 = genWords(symbols, n-1)
    # print(lst1)
    # return [w+v for w in lst1 for v in symbols]

def main():
    lstA = genWords3("abc")
    print(lstA)

    lstB = genWords("abc", 3)  # should return the same words, maybe in other order
    print(lstB)
    assert sorted(lstA) == sorted(lstB)

    lstC = genWords("01", 4)  # should return all length-4 binary words
    print(lstC)

if __name__ == "__main__":
    main()

