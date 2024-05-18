from json import load
f = open("C:\\Users\\rosha\\OneDrive\\Desktop\\mypython works luminar\\languagefundementals\\json_works\\students.json", "r")
result = load(f)

all_names = [n.get("name") for n in result]
print(all_names)

all_departments = {d.get("department") for d in result}
print(all_departments)

max_sal =max(result, key = lambda sal: sal.get("salary")) 
print(max_sal)