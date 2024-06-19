#variables:
# a,b,c=10,20,30
# b=20
# c=30
# print(a+b)

# a=int(input("Enter a first number:"))
# b=int(input("Enter a second number:"))
# print(a+b)

#Datatypes:
# a="siddarth"

# a="""siddarth
# # prachi"""
# print(len(a))                     

# a,b=10,20
# c=a+b
# print(c)
# print(type(c))
# c,b=10,20
# a=f"siddarth {c} prachi {b} "
# print(a)
# print(a.format(10,20))

# a="sidduuu"
# print(a[-5:-2])

#Opearators:

# a,b=int(input("enter your first number ")) , int(input("enter your second number "))

# c=a+b
# print("Addition=",c)
# print(type(c))

# c=a-b
# print("substraction=",c)

# c=a*b
# print("Multiplication=",c)

# c=a/b
# print("Division=",c)

# c=a%b
# print("modolus=",c)

# s="siddarth prachi"
# print(len(s))
# print(s.endswith("rth"))
# print(s.count("d"))
# print(s.capitalize())
# print(s.find("prachi"))
# print(s.replace("prachi","sonuuu"))

# print(s[1:8:3])

# a,b=int(input("enter first number")),int(input("enter second number"))
# print("Addition=",a+b)

# print("Substraction=",a-b)


# print("Multiplication=",a*b)

# print("Division=",a/b)

# print("Moduls=",a%b)
# print(type(a+b))

# print(type(a-b))

#String:

# str="prachi"
# print(str.endswith("chi"))

# str="siddarth"
# print(str.count("d"))

# print(str.capitalize())

# str="siddarth omkar prachi"
# print(str.find("omkar"))

# print(str.replace("omkar", "prachi"))

# # str="Samruddhi"
# print(str.casefold())

# print(str.index("omkar"))

# print(str.split( " "))

# Friends=["prachi", "siddarth", "omkar", "Samruddhi",7,False]

#List:

# l1=[1,2,3,4,5]
# print(l1[2])

# print(l1[3])

# print(l1[1:-1])

# print(l1[ : :2])

# print(l1[ : :-1])

# l1=[1,3,2,4,5]
# l1.sort()
# print(l1)

# l1.reverse()
# print(l1)

# l1.append(6)
# print(l1)

# l1.extend([10,20,30,40,50])
# print(l1)

# l1.insert(2,"prachi")
# print(l1)

# l1.pop(0)
# print(l1)

# l1.remove(5)
# print(l1)

#Tuple:

# t1=("prachi","siddarth","samruddhi","prachi")

# print(t1.count("prachi"))

# print(t1.index("siddarth"))   

#Dictionary:                  

# dic={"name":"prachi",
#       "from":"pune",
#       "marks":[80,75,70]}
# print(dic.items())

# print(dic.keys())

# dic.update({10:"siddarth"})
# print(dic)

# print(dic.get("name"))

#Set:

# s={1,8,2,3}
# s.remove(8)
# s.pop()
# print(s.union({4,5,6}))
# print(s.intersection({3,4,8}))

#Conditional Statements:
# 1.If else statement:

# a,b,c=10,20,30

# if(a>b):
#     if(a>c):
#         print("a is gratest number")
#     else:
#         print("c is gratest number")
# else:
#     if(b>c):
#         print("b is greatest number")
#     else:
#         print("c is greatest number")

# 2.if elif else statement:
        
# a=3
# if(a>15):
#     print("Number is greater than 15")
# elif(a>10):
#     print("Number is greater than 10")
# elif(a>5):
#     print("Number is greater than 5")
# else:
#     print("Number is smaller than 5")
    
# 3.Nested if else statement:

# prachi=int(input("Enter age of first girl:"))
# samruddhi=int(input("Enter age of second girl:"))
# sanika=int(input("Enter age of third girl:"))

# if(prachi>samruddhi):
#     if(prachi>sanika):
#         print("prachi is older")
#     else:
#         print("sanika is older")
# else:
#     if(samruddhi>sanika):
#         print("samruddhi is older")
#     else:
#         print("sanika is older") 
           

# stop=input("Enter your stop:")
# if(stop=="Narayangaon"):
#     print("you are in same stop")
# elif(stop=="Hivare"):
#     print("your stop no is 1")
# elif(stop=="khodad"):
#     print("your stop no is 2")
# elif(stop=="shiroli"):
#     print("your stop no is 3")
# elif(stop=="Nimgaon Sawa"):
#     print("your stop no is 4")
# elif(stop=="Paragaon"):
#     print("your stop no is 5")
# else:
#     print("you are in wrong bus")

# l1=[1,2,3]
# l2=[4,5,6]
# l3=[7,8,9]
# l4=l1+l2+l3
# print(l4)

# Examples for practice:

# WT=float(input("Enter your web technology marks:"))
# DBMS=float(input("Enter your DBMS marks:"))
# AI=float(input("Enter your Artificial Intellifence marks:"))
# HCI=float(input("Enter your Human computer interface marks:"))
# CN=float(input("Enter your computer network marks:"))

# total=WT+DBMS+AI+HCI+CN.
# print("your total marks is ",total)

# mark=(total*100)/500
# print("your percentage is ",mark)

# if(mark>=80):
#     print("you got first class with dstinction")
# elif(mark>=70):
#     print("you got first class")
# elif(mark>=60):
#     print("you got higher secondary clas")
# elif(mark>=50):
#     print("you got secondary class")
# elif(mark>=30):
#     print("you got a third class")
# else:
#     print("you are fail Better Luck Next time")


# Emp_name=input("Enter your name: ")
# Basic_salary=int(input("enter your basic salary: "))
# HRA=(Basic_salary*15)/100
# TA=(Basic_salary*10)/100
# DA=(Basic_salary*5)/100

# Gross_salary=HRA+TA+DA+Basic_salary
# print("Heyy ",Emp_name)
# print("your gross salary: ",Gross_salary)
# print("your basic salary: ",Basic_salary)
# print("your HRA: ",HRA)
# print("your TA: ",TA)
# print("your DA: ",DA)



# if(Gross_salary>=400000):
#     print("your post is Manager")
# elif(Gross_salary>=300000):
#     print("your post is SDE-3")
# elif(Gross_salary>=200000):
#     print("your post is SDE-2")
# elif(Gross_salary>=100000):
#     print("your post is SDE-1")
# else:
#     print("your post is Intern")

#Loops:
# 1.While loop:   

# i=0
# while i<=3:
#     print("prachi")
#     i+=1


# l=[1,2,3,4,5,6,7,8,9,10,11,12]
    
# i=0
# while i<l[-1]:
#     print(l[i])
#     i+=1
    

# i=0
# while i<=10
#     print(i)
#     i+=1

# 2.for loop:
    
# l=[1,7,8]
# for i in l:
#     print(i)    

# l=[1,7,8]
# for i in l:
#     print(i)
# else:
#     print("Done")

# For loop with range function:
    
# for i in range(1,10,):
#     print(i)

# for i in range (1,10):
#     print("prachi")

#Break statement:

# for i in range(5):
#     if(i==3):
#         break
#     print(i)
# else:
#     print("Done")

# Continue statement:

# for i in range (5):
#     if(i==1):
#         continue
#     print(i)
# else:
#     print("Done")

# for i in range (5):
#     if (i==3):
#         continue
#     print(i)
# else:
#     print("Done")
    
# for i in range (6):
#     print(i)
#     if(i==3):
#         break
    
#for i in range (5):
#     if (i==3):
#         continue
#      print(i)
# else:
#     print("Done")

# Pass staements:
    
# for i in range(4):
#     pass


# for i in range (1,10,2):
#     print(i)

# even=[]
# odd=[]
# n=int(input("Enter the number:"))
# for i in range (n):
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print("even=",even)
# print("odd=",odd)


# n=int(input("Enter the number:"))
# for i in range (2,n):
#     if n%i==0:
#         print(f"Entered number {n} is not prime number")
#         break
#     else:
#         print(f"Entered number {n} is prime number")
#         break
    
# n=int(input("Enter the number:"))
# for i in range(1,11):
#     print(f"{n} x  {i} =",n*i)

# Home work class:
    

     # swap two number
    # a=10
    # b=20
    # b=20
    # a=10
    # palindrome number -121
    # palindrome string - madam
    
# a,b=10,20
# print("before swaping a=",a,"b=",b)
# temp=a
# a=b
# b=temp
# print("after swaping a=",a,"b=",b)

# a=10
# b=20
# a,b=b,a
# print(a,b)

# a=10
# b=20
# a=a+b
# b=a-b
# a=a-b

# s="madam"
# s1=reversed(s)

# if list(s1)==list(s):
    
#     print("This string is palindrome")
# else:
#     print("This string is not palindrome")
          
# n=121
# temp=n
# reverse=0
# while temp>0:
#     reminder=temp%10
#     reverse=(reverse*10)+reminder
#     temp=temp//10
# if reverse==n:
#     print("This string is palindrome")
# else: 
#     print("This string is not palindrome")
    

# class test:
#     hall=""
#     bed=""
#     kitchen=""
    
# sanika=test()
# sam=test()
# prachi=test()

# sanika.hall="playing room"
# sanika.bed="programming room"
# sanika.kitchen="bedroom"

    

# sam.hall="programming room"
# sam.bed="bedroom"
# sam.kitchen="playing room"

# prachi.hall="programming room"
# prachi.bed="bedroom"
# prachi.kitchen="kitchen"

# print("This is ",sanika.hall)

# class test:
#     def printing(self,name):
#         print("welcome ",name)
        
# a=test()
# a.printing("prachi")           

# class test:
#     def addition(self,a,b):
#         print("addidtion= ",a+b)
# add=test()
# add.addition(10,20)   


# class test:
#     def __init__(self,msg,name):
#         self.m=msg
#         self.n=name
#     def printing(self):
#         print(self.m,self.n)
# a=test("welcome ","prachi")
# a.printing()

# class test:
#     def __init__(self,name,mob_no,email):
#         self.n=name
#         self.m=mob_no
#         self.e=email
#     def printing(self):
#         print(self.n,self.m,self.e)
# name=input("Name of studednt: ")
# mob_no=int(input("mob_no of student:"))
# email=input("Email of student: ")

# a=test(name,mob_no,email)
# a.printing()


#single inheritance:

# class madhukar:
#     def printing1(self):
#         print("bike")
        
# class prachi(madhukar):
#     def printing2(self):
#         print("cycle")
# m=madhukar()
# p=prachi()
# m.printing1()
# p.printing2()
# p.printing1()

#Multiple inheritance:

# class madhukar:
#     def print_madhukar(self):
#         print("hii i am a madhukar father of prachi")
        
# class pooja:
#     def print_pooja(self):
#         print("hii i am a pooja mother of prachi")
        
# class prachi(madhukar,pooja):
#     def print_prachi(self):
#         print("hii i am a prachi daughter of pooja and madhukar")
        
# p=prachi()
# p.print_madhukar()
# p.print_pooja()
# p.print_prachi()

#Multilevel inheritance:

# class madhukar:
#     def print_madhukar(self):
#         print("hii i am a madhukar father of prachi")

# class prachi(madhukar):
#     def print_prachi(self):
#         print("hii i am a prachi mother of shiv")

# class shiv(prachi):
#     def print_shiv(self):
#         print("hii i am a shiv son of prachi")

# s=shiv()
# s.print_madhukar()
# s.print_prachi()
# s.print_shiv()

# class marks:
#     def __init__(self,wt,hci,ai,dbms,cn):
#         self.wt = wt
#         self.hci = hci
#         self.ai = ai
#         self.dbms = dbms
#         self.cn = cn

#     def calc(self):
#         total=self.wt+self.hci+self.ai+self.dbms+self.cn
#         self.avrg=(total*100)/500
#         print("your total marks is: ",total)
#         print("your average marks is: ",self.avrg)
        
#     def rank(self):
#         if(self.avrg>=80):
#             print("you got first class with dstinction")
#         elif(self.avrg>=70):
#             print("you got first class")
#         elif(self.avrg>=60):
#             print("you got higher secondary clas")
#         elif(self.avrg>=50):
#             print("you got secondary class")
#         elif(self.avrg>=30):
#             print("you got a third class")
#         else:
#             print("you are fail Better Luck Next time")
            
# prachi=marks(int(input("Enter your marks:\n WT: ")),int(input("HCI: ")),int(input("AI: ")),int(input("DBMS: ")),int(input("CN: ")))

# prachi.calc()
# prachi.rank()

# siddarth=marks(int(input("Enter your marks:\n WT: ")),int(input("HCI: ")),int(input("AI: ")),int(input("DBMS: ")),int(input("CN: ")))

# siddarth.calc()
# siddarth.rank()

# omkar=marks(int(input("Enter your marks:\n WT: ")),int(input("HCI: ")),int(input("AI: ")),int(input("DBMS: ")),int(input("CN: ")))

# omkar.calc()
# omkar.rank()


# a=10
# b=0
# c=a/b
# print(c)
# try:
#     print(a/b)
# except Exception as e:
#     print(e)

#practice:
  
# class test:
#     def __init__(self,name1,name2):
#         self.name1=name1  
#         self.name2=name2
#     def display(self):
#         print(self.name1,self.name2)
# a=test("prachi","siddarth")
# a.display()
        
# class test:
#     def __init__(self,name):
#         self.name=name
#     def display(self):
#         print(self.name)
# a=test("prachi")
# b=test("siddarth")
# a.display()
# b.display()   


     
        

            
        
        
        


          

    
    
