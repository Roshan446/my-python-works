text = "ABBCDA"
wc = {}
nc = []
for w in text:
    if w in wc:
        wc[w] +=1
        nc.append(w)
        pass
    else:
       wc[w] = 1

print(nc[1])