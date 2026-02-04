trip = {
    "Trip id" : " UB12345",
    "pickup" : "Kondapur",
    "drop" : "Airport",
    "fare" : 450,
    "driver" : "Ravi",
    "status" : "Arriving"

}

print(trip["pickup"])

print(trip.get('Airport') )

print(trip.keys())

print(trip.values())

for key,value in trip.items():
    print (key, ":", value) 

trip.update({"car model" : "Swift Dzire"})

print(trip)

trip.update({"car model" : "Toyota Innova"})

print(trip)

trip.pop("status")
print(trip)

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