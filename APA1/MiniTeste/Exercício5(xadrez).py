inputStr="b8"

def local(inputStr):
    if inputStr[0] == ('a' or 'h') and (inputStr[1] == '1' or inputStr[1] == '8'):
        return "Corner"
    elif inputStr[0] == ("a" or "h") or (inputStr[1] == '1' or inputStr[1] == '8'):
        return "Border"
    else:
        return "Inside"

print(local(inputStr))