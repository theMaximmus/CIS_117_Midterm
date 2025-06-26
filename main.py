# CIS117 - Midterm Part 1 - Maksym Stesev, Micole Chen, Samantha Chin (Team SF Pythons)
#
#

# Constants for the food prices
PRICE_DE_ANZA_BURGER = 5.25 # De Anza Burger
PRICE_BACON_CHEESE = 5.75 # Bacon Cheese
PRICE_MUSHROOM_SWISS = 5.95 # Mushroom Swiss
PRICE_WESTERN_BURGER = 5.95 # Western Burger
PRICE_DON_CALI_BURGER = 5.95 # Don Cali Burger

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
            user_menu_choice = int(input("What burger do you want? (Enter 1-5): "))

            # Check if user wants to exit and terminate the process (return a None value)
            if (user_menu_choice == 6):
                return None
            # End the loop
            loopFlag = True
        except ValueError:
            print("Error, please enter numeric input.")

    # Reset flag variable
    loopFlag = False

    # Loop through the input for the second time
    while not loopFlag:
        try:
            # Ask for the quantity
            amount = int(input("How many of it do you want? (Enter a number): "))

            # End the loop
            loopFlag = True
        except ValueError:
            print("Error, please enter numeric input.")

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

    # Ask user if they are a Student
    isStudentString = input("Are you a student? (y/n): ")
    if (isStudentString == "y"):
        isStudent = True
    else:
        isStudent = False

    # Return the values
    return quantity1, quantity2, quantity3, quantity4, quantity5, isStudent


def compute_bill(user_input):
    '''
    Computes the bill
    :return:
    '''
    burgers = [0, 0, 0, 0, 0]
    for i in range(0, 5):
        burgers[i] = user_input[i]

    # calculating the total bill
    prices = [0.0, 0.0, 0.0, 0.0, 0.0]
    for item in burgers:
        prices[i]
    price_before_tax = burger1 + burger2 + burger3 + burger4 + burger5

    # factoring in tax
    if isStudent == False:
        order_tax = TAX * price_before_tax
    else:
        order_tax = 0

    # Calculate the price after tax
    price_after_tax = float(price_before_tax) + order_tax

    # Return the values
    return order_tax, price_before_tax, price_after_tax

def print_bill(items, tax_amount, price_before_tax, price_after_tax):
    '''
    Prints the bill to the user
    :return:
    '''

    print("*" * 10)
    print("Your bill:")
    print("You ordered:")
    print()

def main():
    display_menu()
    user_input = get_inputs()
    tax_amount, price_before_tax, price_after_tax = compute_bill(user_input)
    print_bill(user_input, tax_amount, price_before_tax, price_after_tax)
    print(user_input)
    print(price_before_tax)
    print(price_after_tax)

main()
