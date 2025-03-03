from datetime import date

def heading():
    # Get today's date
    today = date.today()
    
    # Information about you
    name = "john doe"
    hometown = "seattle, USA"
    major = "Technology Project "
    hobbies = "Reading, Cooking, Hiking"
    activities = "A businessman"
    
    # Create the heading box with asterisks
    print("*" * 40)
    print(f"Name: {name} \\")
    print(f"Hometown: {hometown} \\")
    print(f"Major: {major} \\")
    print(f"Hobbies: {hobbies} \\")
    print(f"Activities: {activities} \\")
    print(f"Today's Date: {today} \\")
    print("*" * 40)

def payroll():
    # Getting user inputs
    employee_name = input("Enter employee's name:  ")
    hours_worked = float(input("Enter the number of hours worked in a week: "))
    hourly_pay_rate = float(input("Enter hourly pay rate: "))
    federal_tax_rate = float(input("Enter federal tax withholding rate (as a decimal): "))
    state_tax_rate = float(input("Enter state tax withholding rate (as a decimal): "))
    
    # Calculating Gross Pay
    gross_pay = hours_worked * hourly_pay_rate
    
    # Calculating Deductions
    federal_withholding = gross_pay * federal_tax_rate
    state_withholding = gross_pay * state_tax_rate
    total_deductions = federal_withholding + state_withholding
    
    # Calculating Net Pay
    net_pay = gross_pay - total_deductions
    
    # Printing the payroll statement
    print("\nPayroll Statement")
    print(f"Employee Name: {employee_name}")
    print(f"Hours worked: {hours_worked}")
    print(f"Hourly Pay Rate: ${hourly_pay_rate:.2f}")
    print(f"Gross Pay: ${gross_pay:.2f}")
    print("Deductions:")
    print(f"  Federal Withholding ({federal_tax_rate * 100:.1f}%): ${federal_withholding:.2f}")
    print(f"  State Withholding ({state_tax_rate * 100:.1f}%): ${state_withholding:.2f}")
    print(f"  Total Deduction: ${total_deductions:.2f}")
    print(f"Net Pay: ${net_pay:.2f}")

def main():
    # Call the heading function
    heading()
    
    # Call the payroll function
    payroll()

# Calling the main function to execute the program
if __name__ == "__main__":
    main()
