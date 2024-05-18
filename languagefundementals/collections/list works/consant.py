lst = ["red", "green", "blue", "white", "black", "apple", "ignore", "under"]
con_wrd =[w for w in lst if w[0] not in ["a", "e", "i", "o", "u"]]
print(con_wrd)