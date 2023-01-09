#building a simple calculator

#user inputs numbers and operator of choice, stores in variables
num1, operator, num2 = input('Enter your calculation:').split()

#numbers get converted from strings to intergers
num1 = int(num1)
num2 = int(num2)

#conditions for the different operators
#solution gets printed
if operator == "+":
    print("{} + {} = {}".format(num1,num2,num1+num2))
elif operator =="-":
     print("{} - {} = {}".format(num1,num2,num1-num2))
elif operator =="*":
     print("{} * {} = {}".format(num1,num2,num1*num2))
elif operator =="/":
     print("{} / {}= {}".format(num1,num2,num1/num2))
elif operator =="%":
     print("{} % {} = {}".format(num1,num2,num1%num2))            
         

