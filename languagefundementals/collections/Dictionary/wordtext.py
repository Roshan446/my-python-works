text = "hello hai hello hai hello hello"
spl_txt = text.split(" ")
wc = {}
for w in spl_txt:
    if w in wc:
        wc[w] +=1
    else:
        wc[w] = 1
print(wc)