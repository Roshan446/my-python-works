#FIZZBUZZ
# print fizz if the numbe ris divisble by 3, print buzz if the number is divisble 5 and print fizz buzz if the number is divisble by 15

num = int(input("please enter the number?"))

if num%15 == 0:
    print("fizz buzz")
elif num%5 == 0:
    print("buzz")
elif num%3 == 0:
    print(" fizz")
else:
    print("goodbye")
