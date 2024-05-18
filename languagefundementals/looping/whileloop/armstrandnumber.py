# num = 153
# sum = 0
# while(num!=0):
#     last_digit = num%10
#     num//= 10
#     sum += last_digit**3
# print(sum)

num = input("enter the number? ")
digits_count = len(num)
num = int(num)
sum = 0
orginal = num
while(num!=0):
    last_digit=  num%10
    num//=10
    sum += last_digit**digits_count
print(f" number  {orginal} is armstorng numebr  " if orginal == sum else f"{orginal} is not an armstrong number")