# Type your code here
user = int(input("Please enter positive number of seconds:"))
minute = 60
hour = 3600
day = 86400

if user < 0:
    print("Invalid!!!")
elif user >= 0:
    days = user / day
    user1=user % day
    godzin = user1/hour
    user2 = (user1 % hour)
    minutes = user2 / minute
    user3 = user2 % minute
    seconds = user3

    print(int(days), "days", int(godzin), "hours", int(minutes), "minutes", int(seconds), "seconds")
