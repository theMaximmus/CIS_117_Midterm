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
            # Take in the first value
            user_menu_choice = int(input("What burger do you want? (Enter 1-5): "))

            if (user_menu_choice == 6):
                break
            loopFlag = True
        except ValueError:
            print("Error, please enter numeric input")

    # Reset flag variable
    loopFlag = False

    # Loop through the input for the second time
    while not loopFlag:
        try:
            # Take in the second value
            amount = int(input("How many of it do you want? "))

            loopFlag = True
        except ValueError:
            print("Error, please enter numeric input")

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

    isStudentString = input("Are you a student? (y/n):")
    if (isStudentString == "y"):
        isStudent = True
    else:
        isStudent = False

    return quantity1, quantity2, quantity3, quantity4, quantity5, isStudent


def compute_bill(quantity1, quantity2, quantity3, quantity4, quantity5, isStudent):
    '''
    Computes the bill
    :return:
    '''
    burger1 = quantity1 * PRICE_DE_ANZA_BURGER
    burger2 = quantity2 * PRICE_BACON_CHEESE
    burger3 = quantity3 * PRICE_MUSHROOM_SWISS
    burger4 = quantity4 * PRICE_WESTERN_BURGER
    burger5 = quantity5 * PRICE_DON_CALI_BURGER

    # calculating the total bill
    price_before_tax = burger1 + burger2 + burger3 + burger4 + burger5

    # factoring in tax
    if isStudent == False:
        order_tax = TAX * price_before_tax
    else:
        order_tax = 0

    price_after_tax = float(price_before_tax) + order_tax
    return price_before_tax, price_after_tax

def print_bill():
    '''
    Prints the bill to the user
    :return:
    '''

def main():
    result = get_inputs()
    price_before_tax, price_after_tax = compute_bill(quantity1, quantity2, quantity3, quantity4, quantity5, isStudent)
    print(result)

main()
