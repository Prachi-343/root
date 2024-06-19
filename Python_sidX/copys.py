def counts(s,n):
    result=""
    if (len(s)>=2):
        for i in range(n):
            result=result+ s[0:2]
    else:
        for i in range(n):
            result=result+s
    print("string copy is: ",result)

st=input("enter your string: ")
no=int(input("no: "))
counts(st,no)

