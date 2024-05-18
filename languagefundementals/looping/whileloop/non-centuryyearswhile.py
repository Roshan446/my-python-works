year = int(input("please enter the desired year? "))
current_year  = 2023
while(year<=current_year):
    if year % 100 != 0:
        print(year)
    year+= 1
