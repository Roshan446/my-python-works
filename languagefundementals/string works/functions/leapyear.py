def is_leapyear(year):
    if year%100 ==0  and year%400 == 0 or year%100!=0 and year%4==0:
        return True
    else:
        return False
print(is_leapyear(2016))


def factorial(num=0):
    fact = 1
    for i in range(1, num+1):
        fact*=i
    return fact
print(factorial(5))
