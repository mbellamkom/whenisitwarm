"""This program will give you the days where the weather is 70 degrees F and above within a user defined time range. """
#Version 0 is using the terminal to receive user input. 
#add datetime module for handling dates
from datetime import datetime
#Program Header
print("When is it Warm?") 
#Ask for a time range 
print("Enter a time range less than or equal to 16 days")
user_defined_time_range_start = input("Enter your start date: mm/dd/yyyy")
user_defined_time_range_end = input("Enter your end date: mm/dd/yyyy")
def date_range():
    try:
        try:
            start_date = datetime.strptime(user_defined_time_range_start, "%m/%d/%Y")
        except ValueError:
            start_date = datetime.strptime(user_defined_time_range_start, "%M/%D/%y")
        try:
            end_date = datetime.strptime(user_defined_time_range_end, "%m/%d/%Y")
        except ValueError:
            end_date = datetime.strptime(user_defined_time_range_end, "%M/%D/%y")
        return start_date, end_date
    except ValueError:
        print("Incorrect format. Please enter mm/dd/yyy.")
        return None, None    
def validate_date_range(start_date, end_date):
    date_range = (end_date - start_date).days
    if date_range > 16:
        return "Error: Date range must be within 16 days"
    elif date_range < 0:
        return "End date must be after start date"
    else: 
        print(f"{date_range} is valid")

def test():
    start_date, end_date = date_range() 
    if start_date == None or end_date == None:
        print("Invalid date range. Please use the mm/dd/yy format.")
    else: 
        result = validate_date_range(start_date, end_date)
        print(result)

if __name__ == "__main__":
    test()    
   
#Debugging code. Remove # to use.
#print(f"Start Date: {user_defined_time_range_start.strftime('%m/%d/%Y')}")
#print(f"End Date: {user_defined_time_range_end.strftime('%m/%d/%Y')}")
regan_national_airport_lattitude = 38.8512
regan_national_airport_longitude = -77.0401
temperature = 72
#from openmeteopy import openmeteopy.daily.dwd.DailyDwd
