class person:
    def __init__(self,name,id):
        self.name = name
        self.id = id
        
class employee(person):
    def __init__(self, name, id,salary,post):
        person.__init__(self,name,id)
        self.salary = salary
        self.post = post
    def Display(self):
        print(self.name)
        print(self.id)
        print(self.salary)
        print(self.post)
        
n=input("enter name ")
i=int(input("enter id "))
s=int(input("enter salary "))
p=input("enter post ")

e1=employee(n,i,s,p)
e1.Display()


        
    