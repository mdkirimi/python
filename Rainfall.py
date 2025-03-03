from datetime import datetime

# Function to display program heading and details
def heading():
    # Get today's date 
    today_date = datetime.now().strftime("%Y-%m-%d")

    # name and other details
    name = "Oumar Guaye"  
    purpose = "Program general purpose"

    # Print the output 
    print('*' * 60)  # Function to display the program heading
    print(f" Name: {name}\\")
    print(f" Purpose: {purpose}\\")
    print(f" Date: {today_date}")
    print('*' * 60)
    
  

# Function to calculate the average rainfall
def calculateAverageRainfall():
    # Asking for the number of years
    years = int(input("Enter the number of years: "))
    
    # Initialize variables to store total rainfall and total months
    total_rainfall = 0
    total_months = 0
    
    # Outer loop for each year
    for year in range(1, years + 1):
        print(f"\nYear {year}:")
        
        # Inner loop for each month of the year
        for month in range(1, 13):
            rainfall = float(input(f"Enter the rainfall (in inches) for month {month}: "))
            total_rainfall += rainfall
            total_months += 1
    
    # Calculating the average rainfall
    average_rainfall = total_rainfall / total_months if total_months != 0 else 0
    
    # Displaying the results
    print("\nResults:")
    print(f"Total months: {total_months}")
    print(f"Total inches of rainfall: {total_rainfall:.2f}")
    print(f"Average rainfall per month: {average_rainfall:.2f} inches")

# Main function
def main():
    heading()  # Calling the heading function
    calculateAverageRainfall()  # Calling the function to calculate and display average rainfall

# Calling the main function to run the program
if __name__ == "__main__":
    main()
