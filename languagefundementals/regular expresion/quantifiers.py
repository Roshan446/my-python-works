from re import *
text = "aaaab CaaaaKedddde7@#"
# pattern = "a*" #any number of a's including zero number
# pattern = "[a-z]*" #any number of lower case alphabets including zero, same for [0-9]* and [A-Z]*
# pattern = "d{2}" #to check where a charcter occurs that no of times 
# pattern = "a{2,4}" #here minimum 2 and maximum 4
pattern = "[0-9]{1,2}"
match_word = finditer(pattern, text)
for m in match_word:
    print(m.start(), m.group())
