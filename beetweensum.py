def prachi(x,y):
    add=x+y
    if add>=15 and add <=20:
        add=20
    else:
        add=x+y
    print("addition is ",add)

a=int(input("enter No: "))
b=int(input("enter No: "))
prachi(a,b)
