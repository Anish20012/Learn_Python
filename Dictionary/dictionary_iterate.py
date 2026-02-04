trip1 = {
    "Trip id" : " UB12345",
    "pickup" : "Kondapur",
    "drop" : ["Airport","Hafeezpet","Hitech city"],
    "fare" : 450,
    "driver" : "Ravi",
    "status" : "Arriving",
    "Trip id" : " UB54321",
}

for k,v in trip1.items(): #duplicate keys will retain the last value
    print (k, ":", v)

print(trip1["drop"][1])

for location in trip1["drop"]:
    print("Drop location option :", location)

trips = [{"Trip id" : " UB12345",
    "pickup" : "Kondapur",
    "drop" : ["Airport","Hafeezpet","Hitech city"],
    "fare" : 450,
    "driver" : "Ravi",
    "status" : "Arriving",
    },
    {"Trip id" : " UB54321",
    "pickup" : "Madhapur",
    "drop" : ["Gachibowli","Miyapur","JNTU"],
    "fare" : 550,
    "driver" : "Suresh",
    "status" : "On Trip",
    }
]

for trip in trips:
    print(trip["Trip id"])