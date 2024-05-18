# write a program  to check whether a year is a leap year or not
# year = int(input("please enter the year? "))
# if year%100 ==0:
#     if year%400 == 0:
#         print("the year is a leap year")
#     else:
#         print("the year is not a leap year")
# elif year%4 == 0:
#     print("the year is a leap year")
# else:
#     print("the year is not a leap year")

year = int(input("enter the year"))
if year%100==0 and year%400 == 0 or year%100!= 0 and year%4==0:
    print(f"the year {year} is a leap year")
else:
    print(f"the year {year} is not a leap year")