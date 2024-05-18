employe = {"id":1000,"name":"hari", "age":25, "department": "developer"}
employe["department"] = "senior developer"
print(employe)

print("salary" in employe)

# employe["salary"] = 45000
# print(employe)

if "salary" not in employe:
    employe["salary"] = 45000
else:
    employe["bonus"] += 10000

print(employe)
if "salary" not in employe:
    employe["salary"] = 45000
else:
    employe["salary"] += 10000

print(employe)