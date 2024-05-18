from re import *
variable  = input("please enter the variable name? ")
rule = "(kl)(-)?[0-9]{2}(-)?[A-Z]{1,2}(-)?[0-9]{4}"
matcher= fullmatch(rule, variable)
print("invalid" if matcher == None else "valid")
