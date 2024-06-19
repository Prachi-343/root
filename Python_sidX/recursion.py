# function def
def facto(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*facto(n-1)

#  function calling 
a= int(input("enter no: "))
print("factorial",facto(a))