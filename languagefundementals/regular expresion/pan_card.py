from re import *
variable = input("please input your pan card no? ")
rule = "[A-Z]{3}[PCAFHT]{1}[A-Z]{1}[0-9]{4}[A-Z]{1}"
matcher = fullmatch(rule, variable)
print("invalid pan card no" if matcher==None else "your pan card no is valid")