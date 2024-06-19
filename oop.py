#example1:
# class Person:
#     def __init__(self,name):
#         self.name = name
#     def display_info(self):
#         print(f"Name is : {self.name}")
    
# class Teacher(Person):
#     def __init__(self,subject,name):
#         self.subject = subject
#         super().__init__(name)
#     def display_info(self):
#         super().display_info()
#         print(f"Subject is : {self.subject}")

# a=Teacher("WT","prachi")
# a.display_info()

#Example2:

# class Teacher:
#     def __init__(self,name):
#         self.name = name
#     def display_info(self):
#         print(f"Name is : {self.name}")

# class Teacher_branch(Teacher):
#     def __init__(self,branch,name):
#         super().__init__(name)
#         self.branch = branch
#     def display_info(self):
#         super().display_info()
#         print(f"Branch is : {self.branch}")

# class Teacher_subject(Teacher_branch):
#     def __init__(self,name,branch,subject):
#         super().__init__(branch,name)
#         self.subject=subject
#     def display_info(self):
#         super().display_info()
#         print(f"Subject is : {self.subject}")

# tech=Teacher_subject(input("Enter your name: "),input("Enter your branch:"),input("Enter your subject: "))
# tech.display_info()

#Example3:

# class vehicle_type:
#     def __init__(self,type):
#         self.type=type
#     def display_info(self):
#         print(f"\nVehicle type is : {self.type}")
        
# class vehicle_brand(vehicle_type):
#     def __init__(self,brand,type):
#         super().__init__(type)
#         self.brand=brand
#     def display_info(self):
#         super().display_info()
#         print(f"Vehicle brand is : {self.brand}")

# class vehicle_model(vehicle_brand):
#     def __init__(self,type,brand,model):
#         super().__init__(brand,type)
#         self.model=model
#     def display_info(self):
#         super().display_info()
#         print(f"Vehicle model is : {self.model}")
#         print("********************************")

# veh1=vehicle_model(input("Enter vehicle type: "),input("Enter vehicle brand: "),input("Enter vehicle model: "))
# print("\n")
# veh2=vehicle_model(input("Enter vehicle type: "),input("Enter vehicle brand: "),input("Enter vehicle model: "))
# print("\n")
# veh3=vehicle_model(input("Enter vehicle type: "),input("Enter vehicle brand: "),input("Enter vehicle model: "))
# print("\n")
# veh4=vehicle_model(input("Enter vehicle type: "),input("Enter vehicle brand: "),input("Enter vehicle model: "))
# print("\n")
# veh5=vehicle_model(input("Enter vehicle type: "),input("Enter vehicle brand: "),input("Enter vehicle model: "))
# print("\n")
# veh6=vehicle_model(input("Enter vehicle type: "),input("Enter vehicle brand: "),input("Enter vehicle model: "))
# print("\n")

# veh1.display_info()
# veh2.display_info()
# veh3.display_info()
# veh4.display_info()
# veh5.display_info()
# veh6.display_info()


#Example4:

# class Animal:
#     def __init__(self,name):
#         self.name = name
#     def display_info(self):
#         print(f"Animal is: {self.name}")
# class Sound(Animal):
#     def __init__(self,name):
#         super().__init__(name)
#         self.name = name
#     def display_info(self):
#         super().display_info()
#         if self.name=="Dog":
#             print("bhauuu bhauuu")
            
#         elif self.name=="Cat":
#             print("mewww mewww")
        
#         elif self.name=="Cow":
#             print("hummm hummm")
        
#         elif self.name=="Monkey":
#             print("talking ")
        
#         elif self.name=="Tiger":
#             print("rorarrrr")
#         else:
#             print("sound not found")
# for i in range(1,7):
#     name=input("Enter animal name: ")        
#     a=Sound(name)
#     a.display_info()        
        
#Access modifier:

#1.Public access modifier:

# class test:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display_info(self):
#         print(f"name is : {self.name}")
        
# t=test("prachi",20)
# t.display_info()
# print(f"age is : {t.age}")

# 2.Protected access modifier:

# class Student:
#     def __init__(self,name,roll_no,branch):
#         self._name=name
#         self._roll_no=roll_no
#         self._branch=branch
#     def display_info(self):
#         print(f"name is : {self._name}")
#         print(f"roll_no is : {self._roll_no}")
        

# class Ranker(Student):
#     def __init__(self,name,roll_no,branch,marks):
#         super().__init__(name,roll_no,branch)
#         self.marks = marks
#     def display_info(self):
#         super().display_info()
#         print(f"branch is : {self._branch}")
#         print(f"marks is : {self.marks}")   

# obj=Ranker("prachi","30","AI&DS","80")
# print(obj._branch)
# obj.display_info()                                     

# Polymorphism:
# class Dog:
#     def __init__(self,name):
#         self.name = name
#     def display_name(self):
#         print(f"Name of dog: {self.name}")

# class Cat:
#     def __init__(self,name):
#         self.name = name
#     def display_name(self):
#         print(f"Name of cat: {self.name}")
    
# d=Dog("kittuuu")
# c=Cat("kittyy")

# def info():
#     c.display_name()
#     d.display_name()
# info()

#property decorator:

# def decorator(function):
#     def inner_decorator():
#         print("This is start of my code : ")
#         function()
#         print("This is end of my code : ")
#     return inner_decorator()

# @decorator
# def test():
#     print(4+5)



# import time
# def decorator(function):
#     def inner_decorator():
#         start=time.time()
#         function()
#         end_time=time.time()
#         print(end_time-start)
#     return inner_decorator()

# @decorator
# def test():
#     for i in range(10):
#         print(i)
        
        

        

        
        
        
        
        
            
           
        




    
        
    
        
        
          
        






        
        