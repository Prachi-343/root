class person:# parent class
    def __init__(self,name,id):#person constructor
        self.name = name
        self.id = id
        
class sid(person):# parent class
    def __init__(self,mo_no,adrss):#person constructor
        self.mo_no = mo_no
        self.adrss = adrss
        
        
class mate(sid):# parent class
    def __init__(self,email,gender):#person constructor
        self.email= email
        self.gender= gender


class employee(mate):#child class
    def __init__(self,salary,post,name,id,mo_no,email,adrss,gender):#employee constructor
       person.__init__(self,name,id)#inheit person constructor
       sid.__init__(self,mo_no,adrss)
       mate.__init__(self,email,gender)
       self.salary =salary
       self.post = post
       
    def display(self):#display function
        print(self.name)
        print(self.id)
        print(self.post)
        print(self.salary)
        print(self.mo_no)
        print(self.email)
        print(self.adrss)
        print(self.gender)

#geting value from user
n=input("enter name ")
i=int(input("entr id "))
p=input("enter post ")
s=int(input("enter Salary "))
m=int(input("enter MO. NO:  "))
e=input("enter email ")
a=input("enter address ")
g=input("enter gender ")

emp1=employee(s,p,n,i,m,e,a,g)#instances or object of employee
emp1.display()
