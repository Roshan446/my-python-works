his_age = int(input("what is the male age? "))
her_age = int(input("please enter the female age? "))
married_status =(input("what is the married status? (True or False)"))

if his_age>= 21 and her_age>= 18 and married_status == True:
    print("proceed")
else:
    print("unable")