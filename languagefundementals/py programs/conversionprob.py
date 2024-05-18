# # # to covert farenheight to degree celsius
# # fh = 280
# # deg_c = (fh - 32) * 5/9
# # print(f"the coversion of 280F to deg  is {deg_c}")
# fh = int(input("what is the farenhiegt value ?" ))
# deg_c = (fh - 32) * 5/9
# print(f"the coversion of 280F to deg  is {deg_c}")


#to find profit percentage
# cost_price = int(input("what is the cost price? "))
# selling_price = int(input("what is the selling preice? "))
# profit = selling_price - cost_price
# profit_perc = (profit/cost_price) * 100
# print(f"the profit percentage is {profit_perc} % ")


#to find bmi 
weight_kg = int(input("enter weight in kg? "))
height_in_cm = int(input("enter height in cm? "))
height_in_m = height_in_cm/100
bmi = weight_kg/height_in_m **2
print(f"your bmi is  {bmi}")