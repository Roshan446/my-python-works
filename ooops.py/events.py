events=[
    
    {"id":1,"name":"mrg","client":"roshan","date":"12-12-2024","place":"ekm","budget":800000},
    {"id":2,"name":"engagement","client":"bilal","date":"12-12-2024","place":"ekm","budget":800000},
    {"id":3,"name":"mrg","client":"manoj","date":"12-12-2024","place":"ekm","budget":800000},
    {"id":4,"name":"birthday","client":"mobin","date":"12-12-2024","place":"ekm","budget":800000},
    {"id":5,"name":"anniversary","client":"soumya","date":"12-12-2024","place":"ekm","budget":800000},
    {"id":6,"name":"meeting","client":"athira","date":"12-12-2024","place":"ekm","budget":800000},
    {"id":7,"name":"xmascelebration","client":"anjali","date":"12-12-2024","place":"ekm","budget":800000},
   

]

# crud
# c=>create
# r=>read 
# u=>update
# d =>delete

event_data= {"id":8,"name":"onamcele","client":"anandhu","date":"12-12-2024","place":"ekm","budget":800000}

# create
events.append(event_data)
# list
# print(events)


# detatil
# id=4
# event_details=[e for e in events if e.get("id") ==id ]
# print(event_details)

# update
# id=1,budget=100000

id=1

upd_events = [e for e in events if e.get("id")==id][0]
upd_events["budget"] =1000000
events.append(upd_events)






