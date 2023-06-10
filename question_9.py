from datetime import datetime, timedelta

def check_date_difference(from_date, to_date, difference):
    # Convert input strings to datetime objects
    date_format = '%y-%m-%d'
    from_datetime = datetime.strptime(from_date, date_format)
    to_datetime = datetime.strptime(to_date, date_format)

    # Calculate the difference in days
    date_difference = abs((to_datetime - from_datetime).days)

    # Check if the difference is less than the specified number of days
    if date_difference < difference:
        return True
    else:
        return False

# Take input from the user
from_date = input("Enter the 'from' date (yy-mm-dd): ")
to_date = input("Enter the 'to' date (yy-mm-dd): ")
difference = int(input("Enter the difference in days: "))

# Call the function and print the result
result = check_date_difference(from_date, to_date, difference)
print(result)
