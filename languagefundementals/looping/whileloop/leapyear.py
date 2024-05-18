year = int(input("enter the year? "))
current_year = 2023
while(year<= current_year):
    if year%100==0 and year%400  == 0 or year%100!=0 and year%4==0:
        print(year)
    year+=1
