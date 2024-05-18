vehicles=[
   
    {"id":1,"name":"passionpro","brand":"hero","price":100000},
    {"id":2,"name":"xpulse","brand":"hero","price":140000},
    {"id":3,"name":"trumph","brand":"triumph","price":300000},
    {"id":4,"name":"hunter","brand":"royal","price":200000},
    {"id":5,"name":"ola s1","brand":"ola","price":170000},
    {"id":6,"name":"ather 400","brand":"ather","price":180000},
]

# for bikes in vehicles:
#     print(bikes.get("name"))

for bikes in vehicles:
    if bikes.get("brand") == "hero":
        print(bikes.get("name"))
for bikes in vehicles:
    if bikes.get("price") > 170000:
        print(bikes.get("name"))

costly_bike = max(vehicles, key = lambda d: d.get("price"))
print(costly_bike)

least_cost_bike = min(vehicles, key = lambda d: d.get("price"))
print(least_cost_bike)