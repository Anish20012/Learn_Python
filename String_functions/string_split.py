message= "your uber booing id is UB12345. Please keep it safe"
booking_id = message.split("is")[1].split(".")[0]
print (booking_id)
booking_id2 = message.split("is")[1].split(".")[0].strip()
print(booking_id2)