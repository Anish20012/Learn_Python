feedback = input("Please give ur feedback : ")

with open("feed_back_log.txt","a") as log:
    log.write(feedback + "\n")

print("Thanks")