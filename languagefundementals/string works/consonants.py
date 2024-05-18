disease = "#12pneumonoultramicroscopicsilicovolcanoconiosis"
v_count = 0
for w in disease:
    if w not in ["a", "e", "i", "o", "u"] and w.isalpha():
        v_count +=1
print(v_count)

print(disease.isalpha())