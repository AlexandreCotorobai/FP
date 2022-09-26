x = input("Cordenadas:")
def local(x):
    list = []
    for i in x:
        list.append(i)
    if ((list[0] == "a" and list[1] == "1") or (list[0] == "a" and list[1] == "8") or (list[0] == "h" and list[1] == "1") or (list[0]== "h" and list[1] == "8")):
        return "Corner"
    elif list[0]=="a" or list[0]=="h" or list[1]=="1" or list[1]=="8":
        return "Border" 
    else:
        return "Inside"

print (local(x))