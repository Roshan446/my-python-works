n1 = int(input("enter number ?"))
n2 = int(input("enter number ?"))
smallest_num = n1 if n1>n2 else n2
i = 1
r = 0
while(i <= smallest_num):
    if n1%i == 0 and n2%i == 0:
        r = i 
    i += 1
print(f"{r} is the hcf of both the numbers" if r!= 1 else "there is no hcf for gthe two numbers")