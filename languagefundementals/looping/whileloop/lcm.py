n1 = int(input("enteer number? "))
n2 = int(input("enteer number? "))
smallest_num = n1 if n1<n2 else n1
i = 1
r = 0
s= 0
while(i <=smallest_num):
    if n1%i == 0 and n2%i == 0:
        r=i
        s = (n1 * n2) / r
    i+= 1    

print(s)