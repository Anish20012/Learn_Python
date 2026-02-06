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

