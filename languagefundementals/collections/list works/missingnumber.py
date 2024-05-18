arr = [1, 3, 4, 5, 6, 7]
arr.sort()

i = 0
while (i<len(arr)):
    ithelment = arr[i]
    jthelemeny = arr[i+1]
    diff = jthelemeny - ithelment
    if diff !=1:
        print(ithelment +1)
        break
