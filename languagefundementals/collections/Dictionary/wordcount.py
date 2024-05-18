text = "hello hai hello hai"
wcount = {}
spl_txt = text.split(" ")
for wc in spl_txt:
    if wc in wcount:
        wcount[wc] += 1
        pass
    else:
        wcount[wc] = 1
print(wcount)