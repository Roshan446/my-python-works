# years = int(input("please enter the year? "))
# current_year = 2023
# century_year  = 100
# for year in range(years,current_year, century_year):
#     print(year)


# years = int(input("please enter the year? "))
# current_year = 2023
# century_year  = 100
# for year in range(years,current_year):
#     if year%100 !=0:
#         print(year)


years = int(input("please enter the year? "))
current_year = 2023
century_year  = 100
for year in range(years,current_year):
    if year%100==0 and year%400  == 0 or year%100!=0 and year%4==0:
        print(year)


