num1 = int(input("please enter the number?"))
num2 = int(input("please enter the number?"))
num3 = int(input("please enter the number?"))
if num1>num2 and num1>num3:
    if num2>num3:
        print(f"{num1},{num2} and {num3} is the sequential  number order")
    else:
        print(f"{num1}, {num3} and {num2} is the sequential  number order")
elif num2>num1 and num2>num3:
    if num1>num3:
         print(f"{num2}, {num1} and {num3} is the sequential  number order")
    else:
        print(f"{num2},{num3} and {num1} is the sequential  number order")
elif num3>num1 and num3>num1:
    if num1>num2:
         print(f"{num3},{num1} and {num2} is the sequential  number order")
    else:
       print(f"{num3}, {num2} and {num1} is the sequential  number order")
else:
    print("the numbers are all equal")