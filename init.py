class salary:
    def __init__(self,basic,n,p):
        name=n
        post=p
        basic_salary=basic
        TA= (basic*25)/100
        DA=(basic *15)/100
        HRA=(basic *30)/100
        gross_salary=(basic_salary + TA +DA + HRA)
        print("*********************************************")
        print("name: ",name + "\npost: ",post + "\nsalary: ",gross_salary)
        print("*********************************************")

print("*************20's Developer's****************")
name1=input("Enter Your Name: ")
post1=input("Enter your Position: ")
bs1=int(input("Enter Your basic salary: "))
emp1=salary(bs1,name1,post1)

name2=input("Enter Your Name: ")
post2=input("Enter your Position: ")
bs2=int(input("Enter Your basic salary: "))
emp2=salary(bs2,name2,post2)

name3=input("Enter Your Name: ")
post3=input("Enter your Position: ")
bs3=int(input("Enter Your basic salary: "))
emp3=salary(bs3,name3,post3)


