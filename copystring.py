def copystr(st,n):
    result=""
    for i in range(n):
        result= result + st
    print(result)
    
s=input("enter your: ")
no=int(input("enter no thats you want to copy the string: "))
copystr(s,no)
