mark = int(input("ENter your mark : "))
attendance = int(input("ENter your attendance : "))

if mark >=50 and attendance>= 70:
    print("Allowed for exam")
else:
    print("NOt allowed for exam")

if mark >=50 or attendance>= 70:
    print("Allowed for exam")
else:
    print("NOt allowed for exam")

order_amount = int(input("Enter order amount : "))
day = "sat"
membership = input("Do u have membership? Y/N")

if (order_amount >= 1000 and day in ['sat','sun']) or membership == 'Y':
    print( "20% discoount applied")
else:
    print("no discount")
