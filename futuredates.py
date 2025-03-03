import datetime

def get_today_date():
    # Get today's date
    return datetime.datetime.now().strftime("%Y-%m-%d")

def display_header(today_date):
    # Output the formatted information
    print("************************************************************")
    print(f"Name: john doe \\")
    print(f"Purpose: Program general purpose \\")
    print(f"Date: {today_date}")
    print("************************************************************")

def get_user_inputs():
    # Input for current day of the week
    today = int(input("Enter today's day of the week (0-6): "))
    # Input for number of days after today
    days_ahead = int(input("Enter the number of days after today: "))
    return today, days_ahead

def calculate_future_day(today, days_ahead):
    # Calculate the future day of the week
    return (today + days_ahead) % 7

def display_future_day(future_day):
    # Days of the week list for output
    days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    # Output the result
    print(f"The future day of the week is {days_of_week[future_day]}.")

def main():
    today_date = get_today_date()
    display_header(today_date)
    today, days_ahead = get_user_inputs()
    future_day = calculate_future_day(today, days_ahead)
    display_future_day(future_day)

if __name__ == "__main__":
    main()
