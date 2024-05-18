from re import *
variable = input("please input variable name? ")
rule = "[k-nK-N][369][a-zA-Z0-9_]*"
matcher = fullmatch(rule, variable)
print("valid" if matcher !=None else "invalid")