class person:
    def __init__(self,name,id):
        self.name = name
        self.id = id
        
class sid:
    def __init__(self,salary,post):
        self.salary = salary
        self.post = post
        
class prachi:
    def __init__(self,email,mo_no):
        self.email = email
        self.mo_no = mo_no
        
class employee(person,sid,prachi):
    def __init__(self,name,id,salary,post,email,mo_no,adress,gender):
        person. __init__(self,name,id)
        sid. __init__(self,salary,post)
        prachi. __init__(self,email,mo_no)
        
        self.adress = adress
        self.gender = gender
        
    def display(self):
        print(self.name)
        print(self.id)
        print(self.salary)
        print(self.post)
        print(self.email)
        print(self.mo_no)
        print(self.adress)
        print(self.gender)
n=input("enter name ")
i=int(input("enter id "))
s=int(input("enter salary "))
p=input("enter post ")
e=input("enter email ")
m=int(input("enter mo_no "))
a=input("enter adress ")
g=input("enter gender ")

emp1=employee(n,i,s,p,e,m,a,g)
emp1.display()
