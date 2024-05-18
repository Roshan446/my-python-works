# to find the sum of all digits in a number

num = 123
sum_of_digits = 0
while (num !=0):
    last_digit = num%10
    sum_of_digits += last_digit
    num//=10
print(sum_of_digits)