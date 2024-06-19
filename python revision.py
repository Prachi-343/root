# 1)Write a Python program to check if a given character is a vowel or a consonant.

# char=input("Enter alphabate:")
# if char=="a":
#     print("Entered alphabate is oval")
# elif char=="e":
#     print("Entered alphabate is oval")
# elif char=="i":
#     print("Entered alphabate is oval")
# elif char=="o":
#     print("Entered alphabate is oval")
# elif char=="u":
#     print("Entered alphabate is oval")
# else:
#     print("Entered alphabate is consonent")
    

# 2)Create a program that takes two numbers as input and prints "Equal" if they are equal, "Not Equal" otherwise.   

# a=int(input("Enter first number:"))
# b=int(input("Enter second number:"))
# if a==b:
#     print("number is equal")
# else:
#     print("number is not equal")


# 3)Write a program to find the largest among three numbers using nested if-else statements.

# a=int(input("Enter first number:"))
# b=int(input("Enter second number:"))
# c=int(input("Enter third number:"))
# if(a>b):
#     if(a>c):
#         print("a  is greater number")
#     else:
#         print("c  is greater number")
# else:
#     if(b>c):
#         print("b  is greater number")
#     else:
#         print("c  is greater number")


# 4)Create a program that prompts the user to enter their birth year and then prints their Chinese zodiac sign.


# 5)Write a Python program to determine the type of triangle based on the lengths of its sides.


# s1=float(input("enter first side:"))
# s2=float(input("enter second side:"))
# s3=float(input("enter third side:"))

# if s1==s2==s3:
#     print("Equilateral triangle")
# elif s1==s2 or s1==s3 or s2==s3:
#     print("Isolated triangle")
    
# elif True:   
#     if s1>s2:
#         if s1>s3:
#             if (s1*s1)==(s2*s2)+(s3*s3):
#                 print("Right angle triangle")
#                 print("s1 is hypotenious")
#         else:
#             if (s3*s3)==(s1*s1)+(s2*s2):
#                 print("Right angle triangle")
#                 print("s3 is hypotenious")
#     else:
#         if s2>s3:
#             if(s2*s2)==(s1*s1)+(s3*s3):
#                 print("Right angle triangle")
#                 print("s2 is hypotenious")
#         else:
#             if (s3*s3)==(s1*s1)+(s2*s2):
#                 print("Right angle triangle")
#                 print("s3 is hypotenious")
               
# else:
#     print("Unknown triangle")



# 1)Write a Python program to check if a given number is even or odd.

# num=int(input("Enter a number:"))
# if num%2==0:
#     print("number is even ")
# else:
#     print("number is odd ")


# 2)Create a program that prompts the user to enter their age and prints whether they are eligible to vote or not.


# age=int(input("Enter age of student: "))
# if age>=18:
#     print("You are eligible to vote")
# else:
#     print("You are not eligible to vote")


# 3)Write a program that takes two numbers as input and prints the larger one.

# a=int(input("Enter first number:"))
# b=int(input("Enter second number: "))
# if a>b:
#     print("a is larger number")
# else:
#     print("b is larger number")


# 4)Create a program that takes three numbers as input and prints them in ascending order.


 # 5)Write a Python program that takes an input number from the user and prints whether it is a prime number or not.


# num=int(input("Enter number: "))
# if num==1 or num==2:
#     print("number is prime and not a number")
# for i in range(2,num):
#     if num% i!=0: 
#         print("prime number",num)
#         break
#     else:
#         print("not prime number",num)
#         break        
        
        
# Write a program that takes three numbers as input and prints the second smallest number.


# a=int(input("Enter first number:"))
# b=int(input("Enter second number:"))
# c=int(input("Enter second number:"))

# if (a>b):
#     if (a>c):
#         if (b>c):
#             print(b)  
#     else:
#         if (a>b):
#             print(a)
# else:
#     if (b>c):
#         if (a>c):
#             print(a)
#     else:
#         if (a>b):
#                 print(a)


# Create a program that prompts the user to enter their exam score and then prints their grade based on the following criteria: 90 or above: A, 80-89: B, 70-79: C, 60-69: D, below 60: F.

# DS=float(input("Enter your ds marks:"))
# CS=float(input("Enter your cs marks:"))
# CC=float(input("Enter your cc marks:"))
# ANN=float(input("Enter your ann marks:"))

# total=DS+CS+CC+ANN
# print("your total marks is",total)

# mark=total/4
# print("your mark is",mark)

# if(mark>=90):
#     print("you got A grade")
# elif(mark>80<=89):
#     print("you got B grade")
# elif(mark>70<=79):
#     print("you got C grade")
# elif(mark>60<=69):
#     print("you got D grade")
# elif(mark<60):
#     print("you are Fail")

# Write a Python program that takes three numbers as input and prints them in descending order without using loops.

# a=int(input("Enter a first number"))
# b=int(input("Enter a second number"))
# c=int(input("Enter a third number"))



# Create a program that prompts the user to enter their birth year and then prints their Chinese zodiac sign based on the Chinese zodiac calendar.


# Write a program that takes an input year and month and prints the number of days in that month (considering leap years for February).



# 1. Design a class hierarchy for a multimedia player. Create a base class Media with attributes title and duration and methods play() and pause(). Then, create subclasses Audio and Video. Ensure that Audio can also adjust volume, and Video can seek to a specific time.

# class Media:
#     def __init__(self, title, duration):
#         self.title = title
#         self.duration = duration
#     def play(self):
#         print("playing",self.title)
#     def pause(self):
#         print("paused")
    
# class Audio(Media):
#     def __init__(self, title, duration):
#         super().__init__(title, duration)
#     def adj_volume(self,volume):
#         print("volume",volume)

# class Video(Media): 
#     def __init__(self, title, duration):
#         super().__init__(title, duration)
#     def seak(self,time):
#         print("seak by",time)

# a=Audio("baby justn ","5")
# a.play()
# a.adj_volume(50)
# a.pause()
# b=Video("big boss","50")
# b.play()
# b.seak(20)
# b.pause()

        
# 2. Implement a class DynamicObject that allows dynamic creation of attributes during runtime, but restricts the deletion of attributes to those defined in its _init_ method.

# 3. Develop a base class Animal with a method make_sound(). Create a subclass Dog that overrides make_sound() to bark. Then, create another subclass Cat that overrides make_sound() to meow. Ensure that each subclass calls the overridden method of its immediate parent using super().

# class Animal:
#     def make_sound(self):
#         print("Animal sound")

# class Dog(Animal):
#     def make_sound(self):
#         super().make_sound()
#         print("bark")

# class Cat(Animal):
#     def make_sound(self):
#         super().make_sound()
#         print("mewww")

# dog=Dog()
# dog.make_sound()
# cat=Cat()
# cat.make_sound()

        
    
# 4. Create a class Student with attributes name, age, and grade. Implement the _init_ method to accept name and age parameters and set grade based on age (e.g., if age < 12, grade is 'Elementary'; if age < 15, grade is 'Middle School', else 'High School').

# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         self.grade=self.setGrade()
#     def setGrade(self):
#         if self.age<12:
#             return("grade is Elementary")
#         elif self.age>15:
#             return("grade is Middle School")
#         else:
#             return("grade is High School")
            
#     def display(self):
#         print("name is", self.name)
#         print("age is", self.age)
#         print("grade is", self.grade)

# s=Student("Prachi",8)
# s.display()
        
    
# 5. Develop a class hierarchy for a vehicle rental system. Create a base class Vehicle with attributes make, model, and year. Then, create subclasses Car, Truck, and SUV. Ensure that each subclass initializes these attributes using super() and provides additional attributes specific to the vehicle type.

# class Vehicle:
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
#     def display(self):
#         print("make",self.make)
#         print("model",self.model)
#         print("year",self.year)

# class Car(Vehicle):
#     def __init__(self, make, model, year,seat):
#         super().__init__(make, model, year)
#         self.seat=seat
#     def display(self):
#         super().display()
#         print("seat",self.seat)
    
# class Truck(Vehicle):
#     def __init__(self, make, model, year,capacity):
#         super().__init__(make, model, year)
#         self.capacity=capacity
#     def display(self):
#         super().display()
#         print("capacity",self.capacity)

# class Suv(Vehicle):
#     def __init__(self, make, model, year,fuel_type):
#         super().__init__(make, model, year)
#         self.fuel_type=fuel_type
#     def display(self):
#         super().display()
#         print("fuel_type",self.fuel_type)

# car=Car("suzuki","ertiga",2021,7)
# car.display()
# truck=Truck("tata","1613",2013,5)
# truck.display()
# suv=Suv("mahendra","thar",2023,"disel")
# suv.display()


# 1. Creating a Class: Define a Python class called Person with attributes name and age. Implement a method called introduce that prints out the name and age of the person.

# 2. Creating Objects: Create two instances of the Person class with different names and ages, and call the introduce method for each object.

# 3. Inheritance - Single: Create a class Student that inherits from the Person class. Add an additional attribute student_id to the Student class. Override the introduce method to include the student's ID.

# 4. Multiple Inheritance: Create two parent classes A and B. Then, create a child class C that inherits from both A and B. Add a method show_info to class C that prints "This is class C".

# 5. Multilevel Inheritance: Define three classes Vehicle, Car, and ElectricCar. Car inherits from Vehicle, and ElectricCar inherits from Car. Each class should have a method drive() which prints a message specific to that class.

# 6. Accessing Parent Class Methods: In a multilevel inheritance scenario similar to the previous question, add a method show_info to the Vehicle class. Then, in the ElectricCar class, call the show_info method of the Vehicle class.

# 7. Overriding Methods: Create a parent class Shape with a method area that returns 0. Then, create child classes Rectangle and Triangle that override the area method to calculate the area of a rectangle and a triangle, respectively.

# 8. Using super(): In a multilevel inheritance scenario, modify the show_info method of the Vehicle class to print "This is a vehicle". Then, in the Car class, use super() to call the show_info method of the Vehicle class, and add "This is a car" to the output.

# 9. Class Variables and Methods: Create a class Employee with a class variable num_of_employees initialized to 0. Increment this variable every time a new employee is created. Implement a class method get_num_of_employees that returns the total number of employees.

# 10. Static Methods: Add a static method is_adult(age) to the Person class that takes an age as input and returns True if the age is 18 or above, otherwise False. 