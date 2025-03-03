def getSales():
    """Gets the salesperson's monthly sales."""
    while True:
        try:
            sales = float(input("Enter the salesperson's monthly sales: $"))
            if sales < 0:
                print("Sales cannot be negative. Please enter a valid amount.")
            else:
                return sales
        except ValueError:
            print("Invalid input. Please enter a numeric value for the sales.")


def getAdvancedPay():
    """Gets the salesperson's advanced pay."""
    while True:
        try:
            advanced_pay = float(input("Enter the amount of advanced pay or 0 if no advance pay was given: $"))
            if advanced_pay < 0:
                print("Advanced pay cannot be negative. Please enter a valid amount.")
            elif advanced_pay > 2000:
                print("Advanced pay cannot exceed $2,000. Please enter a valid amount.")
            else:
                return advanced_pay
        except ValueError:
            print("Invalid input. Please enter a numeric value for the advanced pay.")


def determineCommissionRate(sales):
    """Determines the commission rate based on the salesperson's monthly sales."""
    if sales < 10000:
        return 0.10  # 10%
    elif 10000 <= sales < 15000:
        return 0.12  # 12%
    elif 15000 <= sales < 18000:
        return 0.14  # 14%
    elif 18000 <= sales < 22000:
        return 0.16  # 16%
    else:
        return 0.18  # 18%


def calculatePay(sales, commission_rate, advanced_pay):
    """Calculates the salesperson's pay."""
    pay = sales * commission_rate - advanced_pay
    return pay


def main():
    """Main function to execute the program."""
    # Step 1: Get the salesperson's monthly sales
    sales = getSales()

    # Step 2: Get the amount of advanced pay
    advanced_pay = getAdvancedPay()

    # Step 3: Determine the commission rate
    commission_rate = determineCommissionRate(sales)

    # Step 4: Calculate the salesperson's pay
    pay = calculatePay(sales, commission_rate, advanced_pay)

    # Display the result
    if pay < 0: 
    
        print(f"The  pay is: ${pay:.2f} \n The salesperson must reimburse the company")
    elif pay <= 0:
        
        print(f"The salesperson needs to reimburse ${abs(pay):.2f} to the company.")
    else:
    
         print(f"The pay is: ${pay:.2f}")





if __name__ == "__main__":
    main()
