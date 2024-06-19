a=int(input())
op=input()
b=int(input())
match op:
    case "+":
        print("add=",a+b)
        
    case "-":
        print("sub=",a-b)
        
    case "*":
        print("mult=",a*b)
    case "/":
        print("div=",a/b)
    case "%":
        print("remainder=",a%b)
    case _:
        print("invalid input")