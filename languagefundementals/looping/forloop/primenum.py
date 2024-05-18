num = int(input("please enter the number? "))
is_prime = True
for  i in range (2,num):
    if num%i == 0:
        is_prime = True
        break
    else:
        is_prime = False
print(f'{num} is prime number ') if is_prime == False else print(f'{num} is not a prime number ')
    
    