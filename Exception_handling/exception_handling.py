try:
    number=int(input("How many items ? "))
    Total = 200* number
    average = Total/number
    print("Avg price", average)

except ZeroDivisionError:
    print("Zero not valid")

print("Proceed")