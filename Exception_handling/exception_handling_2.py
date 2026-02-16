try:
    number=int(input("How many items ? "))
    Total = 200* number
    average = Total/number
    print("Avg price", average)

except Exception:0
    print("Zero not valid")

print("Proceed")