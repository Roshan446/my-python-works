# last digit calculator(432, 234,123,453, 567, op = "+")

def diff(*args, **kwargs):
    last_digit = [n%10 for n in args]
    value = kwargs.get("op")
    diff = 0
    if value == "+":
        diff = sum(last_digit)
    elif value =="-":
        for r in last_digit:
           diff -= r
    else:
        for r in last_digit:
            diff *= r
    return diff

print(diff(1,2,3,5,5,8,9, op="-"))