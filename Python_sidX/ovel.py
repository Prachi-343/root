def countovel(o):
    match o:
        case "a":
            print("%s is ovel"%o)
        case "e":
            print("%s is ovel"%o)
        case "i":
            print("%s is ovel"%o)
        case "o":
            print("%s is ovel"%o)
        case "u":
            print("%s is ovel"%o)
        case "A":
            print("%s is ovel"%o)
        case "E":
            print("%s is ovel"%o)
        case "I":
            print("%s is ovel"%o)
        case "O":
            print("%s is ovel"%o)
        case "U":
            print("%s is ovel"%o)
        case _:
            print("%s is not ovel"%o)
S=input("enter ovel: ")
countovel(S)
