def armstrong_number(num):
    w =len(str(num))
    original = num
    sum = 0
    last_digit = 0
    while num!=0:
        last_digit = num%10
        num = num//10
        sum +=last_digit**w
    print(f'{original} is armstrong is a number' if sum == original else f'{original} is not an armstrong number')

armstrong_number(153)