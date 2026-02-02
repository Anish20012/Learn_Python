mark = int(input("Enter your marks : "))

if mark >= 90:
    print ("Grade A")
elif mark >= 70:
    print ("Grade B") 
elif mark >= 50:
    print ("Grade C")
else:
    print ("Fail")

age = int(input("ENter your age : "))
licence = input("Do you have licence? Y/N ")

if age >= 18:
    if licence == "Y":
        print("You can drive")
    else:
        print("Please apply for licence")
else:
    print ("Your are under age")

       