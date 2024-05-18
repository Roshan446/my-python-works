f = open("C:\\Users\\rosha\\OneDrive\\Desktop\\mypython works luminar\\languagefundementals\\filelo\\news.txt", "r")
w_dict = {}

for line in f:
    w = line.rstrip().rsplit(" ")
    for wc in w:
        if wc in w_dict:
            w_dict[wc] +=1
        else:
            w_dict[wc] = 1
print(w_dict)