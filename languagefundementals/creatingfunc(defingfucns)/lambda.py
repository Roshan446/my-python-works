cube = lambda n1:n1**3
print(cube(3))


def is_number(num):
    return "+ve" if num >0 else "-ve" if num<0 else "zero"
print(is_number(-5))

# ^

# converting the above function to lambda function

w =lambda num: "+ve" if num>0 else "-ve" if num <0 else "Zero"
print(w(-5))

max_num = lambda num1,num2: f'{num1} is greater' if num1>num2 else f'{num2} is the greater number'
print(max_num(2,10))



