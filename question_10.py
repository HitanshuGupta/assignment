from datetime import datetime, timedelta

def get_date_before(date, n):
    date_format = '%y-%m-%d'
    input_date = datetime.strptime(date, date_format)
    new_date = input_date - timedelta(days=n)
    return new_date.strftime(date_format)

# Example usage
date = input("Enter the date (yy-mm-dd): ")
n = int(input("Enter the integer: "))

result = get_date_before(date, n)
print(result)
