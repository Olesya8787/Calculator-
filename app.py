
from func_tools.divide import divide
from func_tools.sum import sum
from func_tools.subtract import subtract
from func_tools.multiply import multiply
from func_tools.square import square

res = 0

is_running = True

while is_running:
    user_choose = input("""
        which operator do you want to use :
        +
        - 
        /
        *
        pow : """
    ) 

    num1 = input("Enter your first number : ")
    num2 = input("Enter your second number : ")

    try :           
        num1 = int(num1)
        num2 = int(num2)                  
    except Exception as err :
        user_choose = ""
        print(err) 

    if user_choose == "+":
        res = sum(num1, num2)
        print(res)

    elif user_choose == "-":
        res = subtract(num1, num2) 
        print(res) 

    elif user_choose == "/":
        res = divide(num1, num2) 
        print(res)    

    elif user_choose == "*":
        res = multiply(num1, num2) 
        print(res)  

    elif user_choose == "pow":
        res = square(num1, num2)
        print(res) 

    else :
        is_running = False            

     