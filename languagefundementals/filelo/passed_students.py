students_path = "C:\\Users\\rosha\\OneDrive\\Desktop\\mypython works luminar\\languagefundementals\\filelo\\students.txt"
failed_path = "C:\\Users\\rosha\\OneDrive\\Desktop\\mypython works luminar\\languagefundementals\\filelo\\failed.txt"
passed_path = "C:\\Users\\rosha\\OneDrive\\Desktop\\mypython works luminar\\languagefundementals\\filelo\\passed.txt"
s = open(students_path, "r")
f =  open(failed_path, "r")
p =  open(passed_path, "w")
failed_list = []
students_list = []
# for st in s:
#    r = st.rstrip("\n")
#    students_list.append(r)

# for fs in f:
#    d = fs.rstrip("\n")
#    failed_list.append(d)

# for st in students_list:
#    if st not in failed_list:
#       p.write(st + "\n")

students_set = {st.rstrip("\n") for st in s}
failed_set = {fs.rstrip("\n") for fs in f}
passed_student = students_set - failed_set

for ps in passed_student:
    p.write(ps + "\n")
