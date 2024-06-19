# *
# **
# ***
# ****
def pyramid(char):
    for i in range(5):
        for j in range(i):
            print(char ,end="")
        print("\n")
        
s=input("enter char: ")
pyramid(s)
