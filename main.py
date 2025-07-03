# CIS117 - Midterm Part 1 - Maksym Stesev, Micole Chen, Samantha Chin
# Team: SF Pythons
# This program simulates a college food court menu system. It presents the users
# with a list of available menu items and their prices. The program then prompts
# the user to select items from the menu, validating their input to ensure only
# valid choices are made. Once the user has finished ordering, the program
# calculates and displays a detailed bill, including the total cost of their
# selected items, the total tax amount, and the total price after tax.

# Constants for the food prices
PRICE_DE_ANZA_BURGER = 5.25 # De Anza Burger
PRICE_BACON_CHEESE = 5.75 # Bacon Cheese
PRICE_MUSHROOM_SWISS = 5.95 # Mushroom Swiss
PRICE_WESTERN_BURGER = 5.95 # Western Burger
PRICE_DON_CALI_BURGER = 5.95 # Don Cali Burger
PRICES_LIST = [PRICE_DE_ANZA_BURGER, PRICE_BACON_CHEESE, PRICE_MUSHROOM_SWISS,
               PRICE_WESTERN_BURGER, PRICE_DON_CALI_BURGER]
# Constants for the tax
TAX = 0.09

# List of Burger Names
BURGER_NAMES = ["De Anza Burger", "Bacon Cheese", "Mushroom Swiss", "Western Burger", "Don Cali Burger"]

def display_menu():
    '''
    Displays the menu options for the Food Court
    '''
    print("*" * 10)
    print("Welcome to the College Food Court!")
    print("Please choose from the following:")
    print("1. De Anza Burger - $5.25")
    print("2. Bacon Cheese - $5.75")
    print("3. Mushroom Swiss - $5.95")
    print("4. Western Burger - $5.95")
    print("5. Don Cali Burger - $5.95")
    print("6. Exit")
    print("*" * 10)

def get_inputs():
    '''
    Gets the input from the user by prompting them to enter corresponding values.
    :return: The quantity of each item and a boolean value whether the customer is a Student.
    '''

    # Create a variable to keep track of the quantity of each item in the order
    quantity1 = quantity2 = quantity3 = quantity4 = quantity5 = 0

    # Create a flag variable
    loopFlag = False

    # Loop through the input for the first time
    while not loopFlag:
        try:
            # Ask for the choice of the burger or if the user wants to exit
            user_menu_choice = int(input("What burger do you want? (Enter 1-5, 6 to exit): "))
            # invalidate user inputs less than 1 or greater than 6
            if (user_menu_choice < 1 or user_menu_choice > 6):
              print("Invalid choice. What burger do you want? (Enter 1-5, 6 to exit): ")
              continue
              
            # Check if user wants to exit and terminate the process (End the loop)
            if (user_menu_choice == 6):
                loopFlag = True
                return quantity1, quantity2, quantity3, quantity4, quantity5

            # Ask for the quantity
            amount = int(input("Please input quantity: "))

            # Determine what item was selected and add desired quantity
            if (user_menu_choice == 1):
                quantity1 += amount
            elif (user_menu_choice == 2):
                quantity2 += amount
            elif (user_menu_choice == 3):
                quantity3 += amount
            elif (user_menu_choice == 4):
                quantity4 += amount
            elif (user_menu_choice == 5):
                quantity5 += amount
        except ValueError:
            # Display the error message
            print("Error, please enter numeric input.")

    # Return the values
    return quantity1, quantity2, quantity3, quantity4, quantity5

def compute_bill(user_input):
    '''
    Computes the final bill
    :return: Returns the values for the amount of taxes,
     the price before taxes and the price after taxes of the overall bill.
    '''
    # Copy and paste the amount for each choice from the menu (set to zero
    # by default for each order)
    choices_amounts = [0, 0, 0, 0, 0]
    for i in range(0, len(user_input)):
        choices_amounts[i] = user_input[i]

    # Calculate the total bill
    price_before_tax = 0.0
    item_details = [] # Stores information about the order
  
    for i in range(len(choices_amounts)):
        if choices_amounts[i] > 0: 
          item_total = choices_amounts[i] * PRICES_LIST[i]
          price_before_tax += item_total
          item_details.append((BURGER_NAMES[i], choices_amounts[i], item_total))

    # Ask user if they are a Student
    isStudentString = input("Are you a student? (y/n): ")
    if (isStudentString == "y"):
        isStudent = True
    else:
        isStudent = False

    # Apply taxes as needed
    if isStudent:
        tax_amount = 0
    else:
        tax_amount = TAX * price_before_tax

    # Calculate the price after tax
    price_after_tax = price_before_tax + tax_amount

    # Return the values
    return item_details, tax_amount, price_before_tax, price_after_tax

def print_bill(item_details, tax_amount, price_before_tax, price_after_tax):
    '''
    Prints the full bill to the user.
    '''

    print() # A blank line
    print("Your bill:")
    print("*" * 50)
  
    for item in item_details: 
      print(f"{item[0]} x {item[1]} - ${item[2]:.2f}")
  
    print("*" * 50)
    print("Total before tax: $%.2f" % price_before_tax)
    print("Tax Amount: $%.2f" % (tax_amount))
    print("Total price after tax: $%.2f" % price_after_tax)

def main():
    # Display the menu
    display_menu()
    # Get user input
    user_input = get_inputs()
    # Process the input and calculate the bill
    item_details, tax_amount, price_before_tax, price_after_tax = compute_bill(user_input)
    # Print the bill
    print_bill(item_details, tax_amount, price_before_tax, price_after_tax)

main()

'''
**********
Welcome to the College Food Court!
Please choose from the following:
1. De Anza Burger - $5.25
2. Bacon Cheese - $5.75
3. Mushroom Swiss - $5.95
4. Western Burger - $5.95
5. Don Cali Burger - $5.95
6. Exit
**********
What burger do you want? (Enter 1-5, 6 to exit): 1
Please input quantity: 1
What burger do you want? (Enter 1-5, 6 to exit): 2
Please input quantity: 1
What burger do you want? (Enter 1-5, 6 to exit): 3
Please input quantity: 1
What burger do you want? (Enter 1-5, 6 to exit): 4
Please input quantity: 1
What burger do you want? (Enter 1-5, 6 to exit): 5
Please input quantity: 1
What burger do you want? (Enter 1-5, 6 to exit): 6
Are you a student? (y/n): y

Your bill:
**************************************************
De Anza Burger x 1 - $5.25
Bacon Cheese x 1 - $5.75
Mushroom Swiss x 1 - $5.95
Western Burger x 1 - $5.95
Don Cali Burger x 1 - $5.95
**************************************************
Total before tax: $28.85
Tax Amount: $0.00
Total price after tax: $28.85


**********
Welcome to the College Food Court!
Please choose from the following:
1. De Anza Burger - $5.25
2. Bacon Cheese - $5.75
3. Mushroom Swiss - $5.95
4. Western Burger - $5.95
5. Don Cali Burger - $5.95
6. Exit
**********
What burger do you want? (Enter 1-5, 6 to exit): 5
Please input quantity: 1
What burger do you want? (Enter 1-5, 6 to exit): 2
Please input quantity: a
Error, please enter numeric input.
What burger do you want? (Enter 1-5, 6 to exit): 2
Please input quantity: 2a
Error, please enter numeric input.
What burger do you want? (Enter 1-5, 6 to exit): Bacon Cheese
Error, please enter numeric input.
What burger do you want? (Enter 1-5, 6 to exit): 2
Please input quantity: 2
What burger do you want? (Enter 1-5, 6 to exit): Fries
Error, please enter numeric input.
What burger do you want? (Enter 1-5, 6 to exit): Soda
Error, please enter numeric input.
What burger do you want? (Enter 1-5, 6 to exit): 1
Please input quantity: 5a
Error, please enter numeric input.
What burger do you want? (Enter 1-5, 6 to exit): 1
Please input quantity: two
Error, please enter numeric input.
What burger do you want? (Enter 1-5, 6 to exit): 1
Please input quantity: 3
What burger do you want? (Enter 1-5, 6 to exit): exit
Error, please enter numeric input.
What burger do you want? (Enter 1-5, 6 to exit): 6
Are you a student? (y/n): n

Your bill:
**************************************************
De Anza Burger x 3 - $15.75
Bacon Cheese x 2 - $11.50
Don Cali Burger x 1 - $5.95
**************************************************
Total before tax: $33.20
Tax Amount: $2.99
Total price after tax: $36.19


What burger do you want? (Enter 1-5, 6 to exit): -1
Invalid choice. What burger do you want? (Enter 1-5, 6 to exit): 
What burger do you want? (Enter 1-5, 6 to exit): 7
Invalid choice. What burger do you want? (Enter 1-5, 6 to exit): 
What burger do you want? (Enter 1-5, 6 to exit): 1
Please input quantity: 1
What burger do you want? (Enter 1-5, 6 to exit): 6
Are you a student? (y/n): y

Your bill:
**************************************************
De Anza Burger x 1 - $5.25
**************************************************
Total before tax: $5.25
Tax Amount: $0.00
Total price after tax: $5.25

'''
