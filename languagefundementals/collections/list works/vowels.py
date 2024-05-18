lst = ["red", "green", "blue", "white", "black", "apple", "ignore", "under"]
wow_wrds =[w for w in lst if w[0] in ["a", "e", "i", "o", "u"]]
print(wow_wrds)