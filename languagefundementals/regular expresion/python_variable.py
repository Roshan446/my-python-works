from re import *
variable = input("please enter the variable name? ")
rule = "[a-zA-Z]{1}[a-zA-Z0-9_]*"
matcher = fullmatch(rule, variable)
print("invalid" if matcher == None else "valid variable")
