text  = "goodmorning"
most_rec = {}
for wc in text:
    if wc in most_rec:
        most_rec[wc]+=1
    else:
        most_rec[wc] = 1
print(most_rec)

