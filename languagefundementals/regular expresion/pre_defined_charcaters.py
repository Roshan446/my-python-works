from re import *
text = "ab CaK7@#"
# pattern = "\d" # 0 -9 
# pattern = "\D" # to exclude the digits 0 - 9
# pattern = "\w" # to get the alphunmeric characters [a-zA-Z0-9]
pattern = "\W" # to get exclude the alphanumeric charcters and to get the speascial characters
matcher = finditer(pattern, text)
for m in matcher:
    print(m.start(), m.group())