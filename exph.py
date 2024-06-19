a=int(input("enter the divisor "))
try:
    print(15/a)
except ArithmeticError:
    print("this is zero division error in function ")
    