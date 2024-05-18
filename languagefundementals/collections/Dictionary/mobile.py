mobile =  {"id":100, "name":"iphone 15", "price": 100000, "imei":2500, "processor": "apple"}

# # print all key values
# print Name
# print price
# update the key value of price to 85000

for k,v in mobile.items():
    print(k,v)


print(mobile.get("name"))

print(mobile.get("price"))

mobile.update({"price":85000})
print(mobile) 

mobile.pop("imei")
print(mobile)

mobile.update({"offers":1000})
print(mobile)

#to add a to the value of a key 
mobile["price"] += 1000


#to check whether a key is present in dictonary returning a boolean value

print("price" in mobile)
