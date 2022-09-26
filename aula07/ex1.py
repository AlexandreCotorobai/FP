
from tkinter import filedialog

name = filedialog.askopenfilename(title="Choose File")

def count(filename):

    with open(filename, 'r', encoding="utf-8") as doc:
        letras = {}
        for line in doc:
            for letter in line:
                if letter.isalpha():
                    letter = letter.lower()
                    if letter not in letras:
                        letras[letter] = 1
                    else:
                        letras[letter] += 1

    for letter in sorted(letras):
        print(letter, letras[letter])

count(name)