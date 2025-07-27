from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now() 
    readable_format = current_date.strftime("%Y-%m-%d %H:%M:%S")
    return readable_format

print("Current Date and Time:", display_current_datetime())

number_of_days = int(input("Enter the number of days to add to the current date: "))
def calculate_future_date():
    future_date = datetime.now() + timedelta(days = number_of_days)
    return future_date.strftime("%Y-%m-%d %H:%M:%S")

print("Future date: ", calculate_future_date())