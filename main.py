# Calender Program

# Importing modules
import calendar
import datetime

# Introduction To The Program
print("\n\t\t\t$$$$$$$$$$$$$$$ Calendar Printing Program $$$$$$$$$$$$$$$\n")
date = datetime.datetime.now()
x = date.strftime("%d-%m-%y")
print(f"Date of Execution: {x}\n")

# Taking User Inputs
year = int(input("Enter the year you want the calendar of: "))
month = int(input("Enter the month you want: "))

# Printing Calendar
print("\nHere's Your Calendar")
print("###########################\n")
cal = calendar.month(year, month)
print(cal)
print("###########################")
