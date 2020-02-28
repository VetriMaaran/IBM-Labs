import calendar  # Importing the calendar module.

year_, month_ = int(input().strip()), int(input().strip())  # Getting year and month as input from the user.

print(calendar.month(year_, month_))
