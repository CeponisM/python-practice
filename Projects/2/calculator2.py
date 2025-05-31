# ### 2. Simple Calculator

# **Description**: Basic arithmetic operations with user input.

# **Practice Goals**:
# - Function creation and organization
# - Error handling for invalid operations
# - Menu-driven program structure

# user input validation
def check_input(input):
    try:
        val = float(input)
        return val
    except ValueError:
        print("Invalid input!")
        return 0

# get a number from user
value = check_input(input("Calculator.\n Enter value: "))

def add(value) -> float:
    by = check_input(input(f"\n add {value} by: "))
    return value + by

def subtract(value) -> float:
    by = check_input(input(f"\n subtract {value} by: "))
    return value - by

def multiply(value) -> float:
    by = check_input(input(f"\n multiply {value} by: "))
    return value * by

def divide(value) -> float:
    by = check_input(input(f"\n divide {value} by: "))
    return value / by

def exponent(value) -> float:
    by = check_input(input(f"\n exponent {value} by: "))
    return value ** by

# user menu option checking
def main_menu_option(option):
    if option in ["1", "+", "add"]:
        value = add(value)
    elif option in ["2", "-", "subtract"]:
        value = subtract(value)
    elif option in ["3", "*", "multiply"]:
        value = multiply(value)
    elif option in ["4", "/", "divide"]:
        value = divide(value)
    elif option in ["5", "^", "exponent"]:
        value = exponent(value)
    elif option in ["6", "clear"]:
        value = 0
        main_menu()
    elif option in ["7", "exit", "Exit"]:
        print("\n Goodbye!")
        return
    else:
        print("Invalid option!")
        main_menu()

# calculator main menu
def main_menu():
    print(f"\n Current value: {value}")
    print("1. add")
    print("2. subtract")
    print("3. multiply")
    print("4. divide")
    print("5. exponent")
    print("6. clear")
    print("7. exit")
    main_menu_option(input().lower())

main_menu()