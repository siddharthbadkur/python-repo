# # class A: 
# #     def __init__(self,name,surname,categorry,marriedstatus):
# #         self.name=name
# #         self.surname=surname
# #         self.categorry=categorry
# #         self.marriedstatus=marriedstatus
                 
# #     def show(self):
# #         print('my name is=',self.name)
# #         print('my surnamne is=',self.surname)
# #         print('my csṭegory is=',self.categorry)
# #         print('my married status is=',self.marriedstatus)
# # obj=A('siddharth','badkur','obc','null')
# # obs=A('arun','patel','obc','null')
# # obj.show()
# # obs.show()
# # print(obj.name)
# # print(obs.name)
# # a=1
# # b=2
# # sum=0
# # def add():
# #     print('from a add function',a)
# # def addition():
# #     print('from a function ',b)
# # add()
# # addition()
# # a=1
# # def great():
# #     a=2
# #     print('value comes from global',a)
 
# #     print('value comes from built-in global ',globals()['a'])    
    
# # great()
# #write a code of a caculater
# def add(x,y):
#     return x+y
# def subtract(x,y):
#     return x-y
# def multiply(x,y):
#     return x*y
# def divid(x,y):
#     return x/y
# while True:
#     print('please select your operation ')
#     print("1.add\n,2.subtract\n,3.multiply\n,4.divide\n,5.off\n")
#     n=int(input('enter your choice(1,2,3,4,5)'))    
#     a=int(input('enter your a number'))
#     b=int(input('enter your b number'))
#     print(type(n),type(a),type(b))
# if n==1:
#     print(a,'+',b,'=',add(a,b))
# elif n==2:
#     print(a,'-',b,'=',subtract(a,b))
     
# elif n==3:
#     print(a,'*',b,'=',multiply,(a,b))
# elif n==4:
#     print(a,'/',b,'=',divide(a,b))  
# elif n==5:
#     Break
# else:
#      print('enter you invalid choice')
 
#map higher order function 
# my_list=[10,20,30,40,50]
# def sqr(n):
#     return n*n
# x=map(sqr,my_list)
# print(x)
# print(list(x))
#with string
# my_str="siddharth"
# def plus(n): 
#     x=ord(n)
#     return chr(x+5)
# x=map(plus,my_str)
# print(x)
# print(list(x))
#filter()higher order function 
# my_list=[60,10,70,90,55,75,10,20,40]
# def sort(n):
#  if n>=70:
#     return True
#  x=filter(sort,my_list)
#  b=(my_list(x))
#  print(b)

# my_number=[10,44,23,45,67,90]    
# def even_num(n):
#     if n%2==0:
#         return True
#     return False
# x=filter(even_num,my_number)
# print(x)
# print(list(x))

# my_number=[10,4,23,45,67,90]   
# def odd_num(n):
#     if n%2!=0:
#         return True
#     return False
# x=filter(odd_num,my_number)
# print(x)
# print(list(x))
 
# x=lambda a,b,c:2*a+2*b+2*c
# print(x(20,30,40))
# #reduce retured signle value as comparision to other function 
# from functools import reduce
# def fun(x,y):
#     return x+y
# x=reduce(fun,[10,34,12]) 
# print(x)
# from functools import reduce
# my_str='siddharth'
# def greater(a,b):
#  if a>b:
#     return a
#  else:
#    return b
#  x=functools,reduce(greater,my_str)
#  print('this is largest char',x)




             


          
          


