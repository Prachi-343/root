class prachi:
    x=10
    y=20
    def __init__(self):
        print(self.x+self.y)
    def fun(self): 
        print("hwllo")
    
        
a=prachi()
del prachi.fun
print(a.fun())
# a.x=10
# a.y=20
# a.add()
