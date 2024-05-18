def armstrong(num):
    digit_count = len(num)
    num = int(num)
    original = num
    while (num!=0):
        last_digit = num%10
        pov = last_digit**digit_count
        sum = sum+pov
        num = num//10
    return (True if sum==original else False)