# Complete este programa como pedido no guião da aula.

def listContacts(dic):
    """Print the contents of the dictionary as a table, one item per row."""
    print("{:>12s} : {}".format("Numero", "Nome"))
    for num in dic:
        print("{:>12s} : {}".format(num, dic[num]))

def filterPartName(contacts, partName):
    """Returns a new dict with the contacts whose names contain partName."""
    ...

def addContact(contacto, contactos):
    dados = contacto.split(": ")
    contactos[dados[1]] = dados[0]
    print(contactos)

def deleteContact(num, contactos):
    contactos.pop(num)
    print(contactos)

def searchContact(num, contactos):
    if num in contactos:
        print(contactos[num])
    else:
        print(num)

def menu():
    """Shows the menu and gets user option."""
    print()
    print("(L)istar contactos")
    print("(A)dicionar contacto")
    print("(R)emover contacto")
    print("Procurar (N)úmero")
    print("Procurar (P)arte do nome")
    print("(T)erminar")
    op = input("opção? ").upper()   # converts to uppercase...
    return op


def main():
    """This is the main function containing the main loop."""

    # The list of contacts (it's actually a dictionary!):
    contactos = {"234370200": "Universidade de Aveiro",
        "727392822": "Cristiano Aveiro",
        "387719992": "Maria Matos",
        "887555987": "Marta Maia",
        "876111333": "Carlos Martins",
        "433162999": "Ana Bacalhau"
        }

    op = ""
    while op != "T":
        op = menu()
        if op == "T":
            print("Fim")
        elif op == "L":
            print("Contactos:")
            listContacts(contactos)
        elif op == "A":
            print("Adicionar contacto:")
            addContact(input("Adicionar contacto (Nome: numero): "), contactos)
        elif op == "R":
            print("Remover contacto")
            deleteContact(input("Numero a deletar: "), contactos)
        elif op == "N":
            searchContact(input("introduza o nr: "), contactos)
        else:
            print("Não implementado!")


# O programa começa aqui
main()

