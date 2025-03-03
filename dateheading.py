import datetime

def main():
    # Get today's date
    today_date = datetime.datetime.now().strftime("%Y-%m-%d")
    
    # Output the formatted information
    print("************************************************************")
    print(f"Name: Your name")
    print(f"Purpose: Program general purpose")
    print(f"Date: {today_date}")
    print("************************************************************")

if __name__ == "__main__":
    main()
