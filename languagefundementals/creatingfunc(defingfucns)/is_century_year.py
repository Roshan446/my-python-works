def is_century_year(year):
    if (year%100==0 and year%400==0) or (year%100!=0 and year%4 ==0):
        print(f'{year} is a leap year')
    else:
        print(f'{year}not a leap year')
    
is_century_year(2020)