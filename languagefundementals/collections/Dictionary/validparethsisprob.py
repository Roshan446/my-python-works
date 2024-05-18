dengue_list = ["ekm", "ekm", "tri", "trv", "trv", "tri", "iduki", "kozhikode","tri"]
wc = {}
nc = []
for w in dengue_list:
    if w in wc:
        wc[w] +=1
    else:
        wc[w] = 1
print(nc)

srt_word = sorted(wc, key =lambda k:wc.get(k),reverse=True)
print(srt_word)
