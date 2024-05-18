# # names = ["manoj", "arpit", "cassey", "raphael", "dhruv", "shankhar"]

# # print(w for w in names if w[0] in ["a","i","o","u","e"] )

# # def experience(exp):
# #     n = experience.get("exp")
# #     return n 



# k = [12, 35, 9, 56, 24,291]

# def swapnum(*args):
#     w = list(args)
#     w[0],w[len(w)-1] = w[len(w)-1], w[0]
#     return w

# print(swapnum(1,2,3,4,5))

# k.sort()
# print(k)


# boys_names = ['Muhammad', 'Aara', 'Advik', 'Atharv', 'Vihaan', 'Kiaan', 'Shivansh', 'Rishaan', 'Ayansh', 'Viraj', 'sam']
# boys_names.sort(key = lambda x: len(x))
# print(boys_names)


# test_list = [5, 6, [], 3, [], [], 9]


# new_test_list = [l for l in test_list if l!=[]]
# print(new_test_list)



# def separtion(*args):
#     fl_list = args
#     int_list = [n for n in fl_list if n>=0]
#     neg_lst = [n for n in fl_list if n<0]
#     new_list = [int_list, neg_lst]
#     return new_list
# print(separtion(1,-1,2,5,7,-20,-24,22))

        


# num = int(input("please enter the number: "))
# fact = num  

# for n in range(num, 0, -1):
#     if n!=num and num%n!=0:
#         fact *= n




# print(fact if fact!=1 else "the number is not a prime number")

        
        

# my_tuple = (1, 2, 3, 4, 5)

# print(min(my_tuple))

# w = my_tuple.index(2)
# print(w)



# n = [1,2,3,4,5,8,0,-1,-3]
# n_tup = ()
# new_lst = []
# r = len(n)
# for g in n:
#     for k in range(0,r): 
#         if n[k]!=g and sum([n[k],g, n[k+1]])==0:
#             new_lst.append((n[k],g, n[k+1]))
#         elif n[k]!=g  and n[k+1] not in n:
#             new_lst.append([n[k], g])


# print(new_lst)
# word_dict = {}
# word_list = []
# n = 1                
# while n<11:
#     words= int(input(f"number {n}: "))
#     word_list.append(words)
#     n+=1
# for w in word_list:
#     if w in word_dict:
#         word_dict[w] +=1
#     else:
#         word_dict[w]=1 


# print([k for k in word_dict])



# w1 = "madaam"
# w2 = "adam"
# n = 0
# w1 = sorted(w1)

# for w in w2:
#     if w in w1:
#         w1.remove(w)
#     else:
#         n+=1
# print(f"{w2} is not an anagram word of madaam" if n>0 else f"{w2} is  an anagram word of {w1}" )


# #      0,1,2,3,4
# lst = [1,2,3,4,5]
# #      5  4 3 2 -1  
# k = int(input("number: "))
# f_lst = lst[-k:]
# s_lst = lst[:-k]
# lst = f_lst + s_lst

# print(lst)

# def rotate(word):
#     word = "hello world"
#     word = word.split(" ")
#     f_wrd = word[-1:]
#     s_wrd = word[:-1]
#     word = f_wrd +s_wrd
#     w = (" ".join(word))
#     return(w)

# print(rotate("hello world"))
    


# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5
# j = ""
# k = 5
# l = 0
# j = chr(65+l)
# for r in range(1,k+1):
#     for col in range(1, r+1):
#         print(j, end=" ")
#     l+=1
#     j = chr(65+l)
#     print()


# for row in range(1,6):
#     for col in range(5 - row):
#         print(" ", end="")
#     for col1 in range(row):
#         print("* ", end="")
#     print()



# n = int(input("please enetr the number: "))
# sum = 0
# j = 0
# for r in range(1, n+1):
#     j= r**2
#     sum = sum+j
# print(sum) 




# 1. Write a Python program that accepts a string and calculates the number of digits and letters.


# def str_char_count(strr):
#     difi_cnt = 0
#     letter_cnt = 0
#     spl_cnt=0
#     n = []
#     for r in strr:
#         if r.isdigit() == True:
#             difi_cnt +=1
#         elif r.isalpha() == True:
#             spl_cnt +=1
#         else:
#             letter_cnt +=1
#     n = [f'letter count:{letter_cnt} special character count:{spl_cnt} digit_count:{difi_cnt} ']
#     return n


# print(str_char_count("roshanpaul446@gmail.com"))


        
# 2.Write a python program to display multiplication table of a number (user input)



# n = int(input("please enter the number: "))

# for i in range(1, 11):
#     print(f' {n}*{i} = {i*n}')

    

# 3.Pattern print
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5



# for r in range(1, 6):
#     for col in range(1, r+1):
#         print(r, end="")
#     print()


    # 2. Write a python program to make combinations of 3 digits


# s = []
# for r in range(10):
#     n= r+2
#     j = r+1
#     if n<10 and j<10:
#      s +=[(f"{r}{n}{j}")]

# print(s)


# 3. Pattern print 
#     *
#    * *
#   *   *
#  *     *
# *       *
#  *     *
#   *   *
#    * *
#     *

for row in range(1,6):
    for col in range(5-row):
        print(" ", end="")
    for col in range(1,row+1):
        print("* ", end="")
    
    print()
    
        