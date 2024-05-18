employe = {"id": 1000, "name":"ram", "salary":45000}


student={"name": "roshan", "rollno":15, "course": "python"}
print(student["course"])

#to obtain the keys of the dictionary products


products = {"apple": 4, "orange": 5, "grapes": 5, "tomato":10}

for k in products.keys():
    print(k)

#to obtain the values from the dictionary
for v in products.values():
    print(v)

#to obtain both key and values of the dictionary we use items()

for k,v in products.items():
    print(k,v)

#to print values of the dictionary for a certain key  we can use get() method
    print(products.get("apple"))


#to update the value of a key
products["apple"] = 10
print(products)


#we use updATE method to update the dictionary
products.update({"apple":15})
print(products)


#we use pop method to remove a key from the dictionary
products.pop("apple")
print(products)