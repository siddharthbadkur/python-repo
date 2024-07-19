
# class Student:  
#     @staticmethod
#     def greet():
#         print('thanks for visit')
#     def greet1(self):
#         print('thanks for visit')
# obj=Student()
# obj.greet()
# Student.greet()
# # Student.greet1()
# obj.greet1()  

#class question 
# class A:
#     def __init__(self):
#         print('constructer apply')
# obj=A()#implicity calling
# obj.__init__()#explicity calling
# print(dir(A))#this is using to know the contructer internally working 

# class student:
#     def __init__(self):
#         print('contructer called---')
#         print(self)
# stu=student()

# class siddharth:
#     def __init__(self,name,surname,subject,college):
#         self.name=name
#         self.surname=surname
#         self.subject=subject
#         self.college=college
#     def batao(self):
#         print('nickname of siddharth =',self.name)
#         print('surname of siddharth =',self.surname) 
#         print('subject of siddharth=',self.subject)
#         print('college of siddharth=',self.college)
# obj=siddharth('siddu','badkur','python','carrer college')
# obj.batao()
# print(obj.name)
# print(siddharth .__doc__)

# class map:
#     def __init__(self,name,roll,marks,city):
#         self.name=name
#         self.roll=roll
#         self.marks=marks
#         self.city=city
#     def init(self,name,roll,marks):
#         self.name=name
#         self.roll=roll
#         self.marks=marks
#     def display(self):
#         print("my name is=",self.name)
#         print("my roll is =",self.roll)
#         print("my marks is =",self.marks)
#         print("my city is",self.city)
# obj=map('siddharth',122112,512,'pipariya')
# print(obj.name)
# print(obj.roll)
# print(obj.marks)
# obj.display()
# class instance: 
#     def __init__(self,name,surname,categorry,marriedstatus):
#         self.name=name
#         self.surname=surname
#         self.categorry=categorry
#         self.marriedstatus=marriedstatus
                 
#     def show(self):
#         print('my name is=',self.name)
#         print('my surnamne is=',self.surname)
#         print('my csṭegory is=',self.categorry)
#         print('my married status is=',self.marriedstatus)
# obj=instance('siddharth','badkur','obc','null')
# obs=instance('arun','patel','obc','null')
# obj.show()
# obs.show()
# print(obj.name)
# print(obs.name)
# print(instance.__dict__)

#multilevel inheritance
# class A:
#     name='neeraj'
#     def m1(self):
#         return "this is m1 world"
# class B(A):
#     age=23
#     def m2(self):
#         print("name=",A.name)
#         print("m1=",self.m1())
# class c(B) :
#     def m3(self):
#         print('age=',B.age)
#         self.m2()
# obj=c()
# obj.m3() 
#multiple inheritance
#MRO=method resollution order#left to rigth search by child class 
# class parent1:
#     def m1(self):
#         print("parentmethod called ")
# class parent2:
#     def m2(self):
#         print("parentmethod 2 called ")  
# class child(parent2,parent1):
#     def m3(self):
#         self.m1() 
#         self.m2()
#         print("this is m 3 world")  
# obj=child()
# obj.m3()  
# solution with supermethod 
# class A:
#     def m1(self):
#           print("this is m1 world")
# class B(A):
 
#     def m1(self):
#         print("this is m1 wold")
#         super().m1()
# obj=B() 
# obj.m1()  

# class sid:
#     fu_name = 'siddharth'
#     def s1(self):
#         print("this is s1 village")
# class bhupu(sid):
#     subject='commerce'
#     def s2(self):
#         print('this is s2 village')
# class arun(bhupu):
#     percent=56.3
#     def s3(self):
#         print('my name is ',sid.fu_name)
#         print('my subject is ',bhupu.subject)
#         print('my percent is',arun.percent)
#         self.s1()
#         self.s2()
# obj=arun()
# obj.s3() 
#polyu morphism
# class A:
#      def new(self,x=0,y=0,z=0):
#         return x+y+z
    
# obj=A()
# print(obj.new(5,6))
# print(obj.new(5,6,7,))
# print(obj.new(5,23))        
# print(obj.new())
#python does,t support function overloading
#if you want to perform overloading so we have to install multidispatch package 
# from multipledispatch import dispatch
# class A:
#     @dispatch(int,int)
#     def add(self,x=0,y=0):
#         print(x+y)
#     @dispatch(int,int,int)
#     def add(self,x=0,y=0,z=0):
#         print(x+y+z)
# obj=A()
# obj.add(12,13)
# obj.add(56,4,10)
# class mehak:
#     def rollchange(self,a=1,b=1,c=1,d=1):
#         return a*b*c*d
# obj=mehak()
# print(obj.rollchange(1,3,4,5))
# print(obj.rollchange(2,2))
# print(obj.rollchange(2,4,5))

#map higher order functions
# tuple=(1,3,4,6,7,9)
# def add(b):
#     return b+b
# x=map(add,tuple)
# print(x)
# print(tuple(x))
# my_str="siddharth"
# def add(n):
#     x=ord(n)
#     return x
# x=map(add,my_str)
# print(x)
# print(list(x))
#encapsulation
#access modifier
# public name='neeraj'
# projected _name='neeraj'
# private __name='neeraj' 
# class student:
#     school="SHSS"
#     def __init__(self,name,age):
#         self.name =name
#         self.age =age
#     def details(self):
#         print("name=",self.name)
#         print("age=",self.age)
#         print("school=",student.school)
# class marks(student):
#       def marks(self,hindi,math):
#           self.hindi = hindi
#           self.math = math
#       def complete_details(self):
#           print("name=",self.name)
#           print("age=",self.age)
#           print("school=",student.school)
#           print("hindi=",self.hindi)
#           print("math=",self.math)
# obj=marks("neeraj",45)
# obj.details()
# obj.marks(85,97)
# obj.complete_details()
# student.name="siddharth"
# student.school="saraswati higher secondary school"        
          
          




# def decorater(x):
#     def wrapper():
#         print("start  work")
#         x()
#         print("stop work")
#     return wrapper
# @decorater
# def orignal_fun():
#     print("this is a orignal function")
# orignal_fun()  
# def decorater(fun):
#     def wraperr():
#         print("welcome to it world")
#         fun()
#         print("thankyou for visit")
#     return wraperr    
# @decorater
# def fun():
#     print("this is it world")
# fun()  
# 
# accesing static variables in two types 
#by using classname 
#by using objname
# class farming:
#     cropsseeds="rice"
#     def __init__ (self,name ,ex ):
#         self.name=name #static veriables inside the constructer
#         self.ex=ex
#         resource='tubewell' 
#     def show(self):
#         print("name=",self.name)
#         print("ex=",self.ex)
        
#         print("croptype=",stu.cropsseeds)
# stu=farming("siddharth",10)
# stu.show()
# print(farming.cropsseeds)
# print(stu.cropsseeds)
# print(dir(farming))
# def fact(num):
#     result=1
#     while num>=1:
#       result=result*num
#       num=num-1
#     return result
# i=int(input('enter your number'))
# print('the factorial of',i,"is:",fact(i))

# fact = fact(i)
# print("Factorial =",fact)
#variable length argument args*
# def add(*x):
#  sum=0
#  for i in x:
#     sum+=i
# print('total number of  sum',sum)
# add()
# add(10)
# add(10,20)
# add(10,20,30)
#variable length keyword argument
# def sum1(n1,**n):
#     sum=0
#     for key in n:
#         sum=sum+n[key]
#         print(sum)
# sum1(n1=10,n2=20)
# sum1(n1=10,n2=20,n3=30)
# sum1(n1=10,n2=20,n3=30,n4=40)        
#global variable in method 
# a=1
# b=2
# def add():
#     print('from a add function',a,b)
# def addition():
#     print('from a function ',a,b)
# add()
# addition()






    







     
   
   
   
   
   
    
             





        
                                
          









        
    


    
        