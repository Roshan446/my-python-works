# num1 = int(input("please enter the number?"))
# num2 = int(input("please enter the number?"))
# num3 = int(input("please enter the number?"))
# if num1>num2 and num1>num3:
#     print(f"{num1} is the greatest number")
# elif num2>num1 and num2>num3:
#     print(f"{num2} is the greates number")
# elif num3>num1 and num3>num1:
#     print(f"{num3}is the greatesr number")
# else:
#     print("the numbers are all equal")



##greates second number

num1 = int(input("please enter the number?"))
num2 = int(input("please enter the number?"))
num3 = int(input("please enter the number?"))
if num1>num2 and num1>num3:
    if num2>num3:
        print(f"{num2} is the 2nd greatest number")
    else:
        print(f"{num3} is the 2nd greatest ")
elif num2>num1 and num2>num3:
    if num1>num3:
        print(f"{num1} is the 2nd greatest number")
    else:
        print(f"{num3} is the 2nd greatest ")
elif num3>num1 and num3>num1:
    if num1>num2:
        print(f"{num1} is the 2nd greatest number")
    else:
        print(f"{num2} is the 2nd greatest ")
else:
    print("the numbers are all equal")
