#Question 1

from datetime import date

def heading():
     name = "Oumar Guaye"
     hometown = "Fort lauderdale, USA"
     major = "Technology Project Management"
     hobbies = "Reading, Cooking, Hicking"
     activities = "A businesman"
     today = date.today().strftime("%B %d, %Y")  

     info = [
         f" Name: {name} \\",
        f" Hometown: {hometown} \\",
        f" Major: {major} \\",
         f" Hobbies: {hobbies} \\",
        f" Activities: {activities} \\",
         f" Date: {today} \\"
     ]
    
     max_length = max(len(line) for line in info)  
     border = "*" * (max_length + 4)

     print(border)
     for line in info:
         print(f" {line.ljust(max_length)} ")
     print(border)



def main():
     heading()

if __name__ == "__main__":
     main()





#Question 2
def calculate_initial_deposit(final_value, annual_rate, years):
    monthly_rate = (annual_rate / 100) / 12  # Convert annual rate to monthly decimal
    months = years * 12  # Convert years to months
    initial_deposit = final_value / ((1 + monthly_rate) ** months)  # Formula
    
    return initial_deposit

def main():
    # Get user input
    final_value = float(input("Enter the final account value: "))
    annual_rate = float(input("Enter the annual interest rate (in %): "))
    years = float(input("Enter the number of years: "))

    # Calculate initial deposit
    initial_deposit = calculate_initial_deposit(final_value, annual_rate, years)

    # Display result
    print(f"\nTo have ${final_value:,.2f} after {years} years,")
    print(f"you need to deposit: ${initial_deposit:,.2f}")

if __name__ == "__main__":
    main()

