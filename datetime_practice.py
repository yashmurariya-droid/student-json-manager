import datetime

today = datetime.date.today()
now = datetime.datetime.now()

print("Today's date:", today)
print("Current time:", now.strftime("%I:%M:%S %p"))