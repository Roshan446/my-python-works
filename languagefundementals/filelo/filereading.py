path =  "C:\\Users\\rosha\\OneDrive\\Desktop\\mypython works luminar\\languagefundementals\\filelo\\centuryyears.txt"
f = open(path, "r")

# f = open(path, "w")

# f.write("hello")
# colors = ["red","blue","green"]
# for c in colors:
#     f.write(c + "\n")


#write all century years from 1800 - 2023

# for years in range(1800, 2025, 100):
#     year = str(years)
#     f.write(year + "\n")

"years from 1800 - 2024" 

# for years in range(1800,2025):
#     year = str(years)
#     f.write(year + "\n")


"read all years from the years.txt that are leap years from 1800 - 2024"

for y in f:
    year = int(y.rstrip("\n"))
    if year%100==0 and year%400==0 or year%100 !=0 and year%4 ==0:
        print(year)

# to write this into a new txt file leap_years.txt
write_path =  "C:\\Users\\rosha\\OneDrive\\Desktop\\mypython works luminar\\languagefundementals\\filelo\\leap_years.txt"
readpath =  "C:\\Users\\rosha\\OneDrive\\Desktop\\mypython works luminar\\languagefundementals\\filelo\\centuryyears.txt"

fr = open(readpath, "r")

fw = open(write_path, "w")

for y in fr:
    year = int(y.rstrip("\n"))
    if year%100==0 and year%400==0 or year%100 !=0 and year%4 ==0:
        
        fw.write(str(year)+ "\n")


