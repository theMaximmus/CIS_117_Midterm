# Team Name: SF Pythons
#
# Team Members:
#
# 1. Maksym Stesev
#
# 2. Micole Chen
#
# 3. Samantha Chin

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

    return quantity1, quantity2, quantity3, quantity4, quantity5


def compute_bill():
    '''
    Computes the bill
    :return:
    '''

def print_bill():
    '''
    Prints the bill to the user
    :return:
    '''

def main():
    result = get_inputs()
    print(result)

main()
