num = int(input("enter the number? "))
prev_value = 0
curr_value = 1
print(prev_value,end=" ,")
print(curr_value, end=" ,")
for i in range(1, num,):
    next_value = prev_value + curr_value
    print(next_value, end=" ,")
    prev_value = curr_value
    curr_value = next_value
    