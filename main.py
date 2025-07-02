# CIS117 - Midterm Part 1 - Maksym Stesev, Micole Chen, Samantha Chin
# Team: SF Pythons
#

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

def display_menu():
    '''
    Displays the menu options for the Food Court
    :return:
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
    Gets the input from the user
    :return:
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

            # Check if user wants to exit and terminate the process (return a None value)
            if (user_menu_choice == 6):
                return 0, 0, 0, 0, 0, False
            # End the loop
            loopFlag = True
        except ValueError:
            print("Error, please enter numeric input.")

    # Loop through the input for the second time
    while not loopFlag:
        while True:  
        try:
            # Ask for the choice of the burger or if the user wants to exit
            user_menu_choice = int(input("What burger do you want? (Enter 1-5, 6 to exit): "))
            amount = int(input("Please input quantity"))
            if (user_menu_choice == 1):
                q1 += amount
            elif (user_menu_choice == 2):
                q2 += amount
            elif (user_menu_choice == 3):
                q3 += amount
            elif (user_menu_choice == 4):
                q4 += amount
            elif (user_menu_choice == 5):
                q5 += amount
            # Check if user wants to exit and terminate the process (return a None value)
            if (user_menu_choice == 6):
                return q1, q2, q3, q4, q5, False
            # End the loop
        except ValueError:
            print("Error, please enter numeric input.")

    # Ask user if they are a Student
      isStudentString = input("Are you a student? (y/n): ")
      if (isStudentString == "y"):
          isStudent = True
      else:
          isStudent = False

    # Return the values
    return quantity1, quantity2, quantity3, quantity4, quantity5, isStudent

def compute_bill(user_input, isStudent):
    '''
    Computes the bill
    :return:
    '''
    # Copy paste the amount for each choice from the menu
    choices_amounts = [0, 0, 0, 0, 0]
    for i in range(0, 5):
        choices_amounts[i] = user_input[i]

    # Calculate the total bill
    price_before_tax = 0.0
    for i in range(len(choices_amounts)):
        price_before_tax += choices_amounts[i] * PRICES_LIST[i]

    # Apply taxes as needed
    if isStudent == True:
        tax_amount = 0
    else:
        tax_amount = TAX * price_before_tax

    # Calculate the price after tax
    price_after_tax = price_before_tax + tax_amount

    # Return the values
    return tax_amount, price_before_tax, price_after_tax

def print_bill(items, tax_amount, price_before_tax, price_after_tax):
    '''
    Prints the bill to the user
    :return:
    '''

    print()
    print("Your bill:")
    print("*" * 50)
    print("You ordered: " + str(items))
    print("*" * 50)
    print("Total before tax: %.2f" % price_before_tax)
    print("Tax Amount: %.2f" % (tax_amount))
    print("Total price after tax: %.2f" % price_after_tax)
    return

def main():
    display_menu()
    user_input = get_inputs()
    tax_amount, price_before_tax, price_after_tax = compute_bill(user_input,
                                                                 user_input[len(user_input)-1])
    print_bill(user_input, tax_amount, price_before_tax, price_after_tax)
    print(user_input)
    print(price_before_tax)
    print(price_after_tax)

main()
