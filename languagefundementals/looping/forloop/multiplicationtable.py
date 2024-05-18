num = int(input("please enter the number? "))
limit = int(input("what is the limit? "))
limit +=1

for i in range(1,limit):
    print(f"{num}*{i}= {i*num}")
