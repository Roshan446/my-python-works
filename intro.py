intrest_rate  =  int(input("please enter the intrest rate?"))
loan_amount = int(input("please enter the loan amount?"))
loan_tenure = int(input("please enter the tenure?"))

total_intrest  = loan_amount*(intrest_rate/100)*loan_tenure
print(total_intrest)
total_payable = loan_amount+total_intrest
emi_month = total_payable/(loan_tenure*12)
print(emi_month)