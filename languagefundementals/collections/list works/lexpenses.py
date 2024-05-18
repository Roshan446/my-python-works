expenses = [10000, 20000, 30000, 50000, 10000, 580000, 200000]
print(expenses[2])

# for i in range(0, len(expenses)):
#     print(expenses[i])

# for exp in expenses:
#     print(exp)


# # Q) print all expenses > than 20000


# for i in range(0, len(expenses)):
#     if expenses[i]>20000:
#         print(expenses[i])

# for exp in expenses:
#     if exp >20000:
#         print(exp)


# for i in range(0, len(expenses)):
#     # # if expenses[i]>15000 and expenses[i] <25000:
#     # #     print(expenses[i])
    
#     # if expenses[i] in range(15000,25000):
#     #     print(expenses[i])


# r = 0
# # for i in range(0, len(expenses)):
# #     if expenses[i]>expenses[r]:
# #         print(expenses[i])
# #     r+=i

mac_value= max(expenses)
print(mac_value)
total_exp = sum(expenses)
print(total_exp)
avg_exp = total_exp//len(expenses)
print(avg_exp)


# max_exp=0
# for i in range(0,len(expenses)):
#     cur_exp=expenses[i]
#     if cur_exp>max_exp:
#         max_exp=cur_exp
# print(max_exp)