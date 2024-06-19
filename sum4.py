def prachi(x,y,z):
    add=0
    if x==y or y==z or x==z:
        add=0
    else:
        add=x+y+z
    print("sum is ",add)

a=int(input("enter NO: "))
b=int(input("enter NO: "))
c=int(input("enter NO: "))
prachi(a,b,c)