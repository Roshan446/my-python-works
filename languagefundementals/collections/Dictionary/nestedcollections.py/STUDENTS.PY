students=[
    {"id":1,"name":"jhon","skills":["c","c++"],"exp":2,"qualification":"mca"},
    {"id":1,"name":"jain","skills":["python","js"],"exp":0,"qualification":"btec"},
    {"id":1,"name":"vijin","skills":["c","java","python"],"exp":4,"qualification":"mca"},
    {"id":1,"name":"tinu","skills":["r","java"],"exp":3,"qualification":"mtech"},
    {"id":1,"name":"roy","skills":["python","css","js"],"exp":0,"qualification":"bca"},
    {"id":1,"name":"vijil","skills":["js","r","css"],"exp":1,"qualification":"mtech"},
    {"id":1,"name":"ravi","skills":["java","python"],"exp":3,"qualification":"btec"},
    {"id":1,"name":"tom","skills":["java","css","r","sql"],"exp":4,"qualification":"bca"},
    {"id":1,"name":"ryan","skills":["c","css","python"],"exp":0,"qualification":"mca"},
]

# # total number of students.

# # print("total no of students is " , len(students))

# #print all student names 

# # for n in students:
# #     print(n.get("name"), end = ",")

# stud_name_exp  = [n.get("name") for n in students]
# print(stud_name_exp)



# # Q print all student names who have an experience greater than 1

# stud_name = [stud.get("name") for stud in students if stud.get("exp")>1]
# print(stud_name)


# #Q print all student names who has skilset oj java and python 


# for stud in students:
#     if "java" in stud.get("skills"):
#         print(stud.get("name"))

# #Q print mca student names
# for stud in students:
#     if "mca" in stud.get("qualification"):
#         print(stud.get("name"))
# #Q4 print all name who has qualification of java and python 

# for stud in students:
#     print(stud.get("name") if "java" in stud.get("skills") and "python" in stud.get("skills") else "")

#q5 print the most experienced student

max_exp = max(students, key = lambda exp:exp.get("exp"))

highest_exp = max_exp.get("exp")
max_exp_stud = [stud.get("name") for stud in students if stud.get("exp")==highest_exp]
print(max_exp_stud)

# Q print all name who have skills  > 2
for stud in students:
    if len(stud.get("skills")) > 2:
        print(stud.get("name"))


#q print all names who name starts with j

for studs in students:
    if str(studs.get("name")).startswith("j"):
        print(studs.get("name"))

#q print the mos selected skills
max_skill =[]
skill_list = []
skill_dict = {}



# for stud in students:
#     skill_list += stud.get("skills")

# for skill in skill_list:
#         if skill in skill_dict:
#             skill_dict[skill] += 1
#         else:
#             skill_dict[skill] = 1

for stud in students:
    skills = stud.get("skills")
    for sk in skills:
        if sk in skill_dict:
            skill_dict[sk] += 1
        else:
            skill_dict[sk] = 1
print(skill_dict)
