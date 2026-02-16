try:
    number=int(input("How many items ? "))
    Total = 200* number
    average = Total/number
    print("Avg price", average)

except FileNotFoundError: # not a valid exception
    print("Zero not valid")
finally:
    print("Always execute incase of pass or error")


print("Proceed")