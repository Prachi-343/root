a=int(input("enter your first no: "))
b=str(input("enter your oprator no: "))
c=int(input("enter your second no: "))
match b:
    case "+":
        cal=a+c
        print(cal)
    case "-":
        cal=a-c
        print(cal)
    case "*":
        cal=a*c
        print(cal)
    case "/":
        cal=a/c
        print(cal)
    case "%":
        cal=a%c
        print(cal)
    case _:
        print("invalid oprator!!")
        
