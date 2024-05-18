
disease  = "pneumonoultramicroscopicsilicovolcanoconiosis"
v_count = 0
for w in disease:
    # if w == "o" or w == "e" or  w == "a" or w =="i" or w == "u":
    if w in ["a", "o", "u", "i", "e"]:
        v_count += 1
print(f'the total number of values is {v_count}')


