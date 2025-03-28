#This program will give you the days where the weather is 70 degrees F and above within a user defined time range. 
#Version 0 is using the terminal to receive user input. 
#add datetime module for handling dates
from datetime import datetime
#Program Header
print("When is it Warm?") 
#Ask for a time range 
#note: the time range limits will have to be determined after looking at the API
user_defined_time_range_start = input("Enter your start date: mm/dd/yy")
user_defined_time_range_end = input("Enter your end date: mm/dd/yy")
#input is returned as string, so convert to date (note: this may have to be a different number format later)
#note: need to handle the user error of trying to write the date as 1/21/2025 instead of 01/21/2025
user_defined_time_range_start = datetime.strptime(user_defined_time_range_start, "%m/%d/%Y")
user_defined_time_range_end = datetime.strptime(user_defined_time_range_end, "%m/%d/%Y")
#Verfiy input is converted/remove after debugging
print(f"Start Date: {user_defined_time_range_start.strftime('%m/%d/%Y')}")
print(f"End Date: {user_defined_time_range_end.strftime('%m/%d/%Y')}")