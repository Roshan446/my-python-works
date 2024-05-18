from re import *
text = "fat-cat-run-fast-catch"
match_word ="at"
matchier = finditer(match_word, text)
count = 0
for m in matchier:
    print(m.start(), m.group())
    count +=1
print(count)