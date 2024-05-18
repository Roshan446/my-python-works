add = lambda n1,n2: n1+n2
# print(add(5,2))

cube = lambda n: n**3
print(cube(3))

num_check = lambda n: "+ve" if n>=0 else "-ve" if n<0 else "zero"
print(num_check(3))


max_num = lambda n1, n2: n1 if n1> n2 else n2
print(max_num(10, 100)) 


odd_eve = lambda n1: "odd" if n1 %2 !=0 else "even"
print(odd_eve(2))



