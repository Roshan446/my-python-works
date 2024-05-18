text = "ABBCDA"
wc = {}
# for w in text:
#     if w in wc:
#         wc[w] +=1
#         break
#     else:
#         wc[w] = 1
# print(w)


for w in text:
    if w in wc:
        wc[w] += 1
    else:
        wc[w] = 1
print(wc)

for k,v in wc.items():
    if(v==1):
        print(k)