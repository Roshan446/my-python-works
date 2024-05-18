f = open("C:\\Users\\rosha\\OneDrive\\Desktop\\mypython works luminar\\languagefundementals\\filelo\\news.txt", "r")

for line in f:
   
    print(len(line.rstrip("\n").split(" ")))

for line in f:
    line.rstrip("\n").split(" ")
    print(line)