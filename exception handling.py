#example2
#exception handling 
# num1=int(input("enter your num1"))
# num2=int(input("enter your num2"))
# try:
#     div=num1/num
#     print("division is ",div)
# except Exception as var:
#   print(var)
#   print(var.__class__)
# print("rest of code execute")
import sys

num1=int(input("enter your num1"))
num2=int(input("enter your num2"))
try:
    div=num1/num #which error comes in first so that error will reflect firstly
    print("division is ",div)
except:
    # print(sys.exc_info()[0])
    print(sys.exc_info()[0])
   
print("rest of code execute")